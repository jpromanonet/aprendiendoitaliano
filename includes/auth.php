<?php

declare(strict_types=1);

function login_session(int $userId): void
{
    session_regenerate_id(true);
    $_SESSION['user_id'] = $userId;
    remember_login($userId);
}

function remember_login(int $userId): void
{
    ensure_remember_column();
    $token = bin2hex(random_bytes(32));
    $stmt = db()->prepare(
        'UPDATE users SET remember_token = ?, remember_expires = DATE_ADD(NOW(), INTERVAL 30 DAY) WHERE id = ?'
    );
    $stmt->execute([hash('sha256', $token), $userId]);
    setcookie('ai_remember', $token, remember_cookie_options(time() + 60 * 60 * 24 * 30));
}

function forget_login(?int $userId): void
{
    if ($userId) {
        ensure_remember_column();
        $stmt = db()->prepare('UPDATE users SET remember_token = NULL, remember_expires = NULL WHERE id = ?');
        $stmt->execute([$userId]);
    }
    setcookie('ai_remember', '', remember_cookie_options(time() - 3600));
}

function user_id_from_remember_cookie(): int
{
    $token = (string) ($_COOKIE['ai_remember'] ?? '');
    if ($token === '') {
        return 0;
    }
    ensure_remember_column();
    $stmt = db()->prepare(
        'SELECT id FROM users WHERE remember_token = ? AND remember_expires > NOW()'
    );
    $stmt->execute([hash('sha256', $token)]);
    return (int) $stmt->fetchColumn();
}

function ensure_remember_column(): void
{
    static $ready = false;
    if ($ready) {
        return;
    }
    $ready = true;
    $exists = db()->query("SHOW COLUMNS FROM users LIKE 'remember_token'")->fetch();
    if ($exists) {
        return;
    }
    db()->exec(
        'ALTER TABLE users
         ADD remember_token CHAR(64) NULL,
         ADD remember_expires DATETIME NULL'
    );
}

function remember_cookie_options(int $expires): array
{
    $path = rtrim((string) config()['base_path'], '/');
    return [
        'expires' => $expires,
        'path' => $path !== '' ? $path : '/',
        'httponly' => true,
        'samesite' => 'Lax',
    ];
}

function create_user(string $email, ?string $password, string $name, ?string $avatar = null): int
{
    $hash = $password !== null && $password !== '' ? password_hash($password, PASSWORD_DEFAULT) : null;
    $stmt = db()->prepare(
        'INSERT INTO users (email, password_hash, display_name, avatar_url, is_admin) VALUES (?, ?, ?, ?, 0)'
    );
    $stmt->execute([$email, $hash, $name, $avatar]);
    return (int) db()->lastInsertId();
}

function find_user_by_email(string $email): ?array
{
    $stmt = db()->prepare('SELECT * FROM users WHERE email = ?');
    $stmt->execute([$email]);
    $row = $stmt->fetch();
    return $row ?: null;
}

function google_configured(): bool
{
    $google = config()['google'];
    return $google['client_id'] !== '' && $google['client_secret'] !== '';
}

function google_start(): void
{
    if (!google_configured()) {
        flash('El ingreso con Google todavía no tiene un cliente OAuth. Mientras tanto podés entrar con correo y contraseña.');
        redirect('cuenta');
    }
    $state = bin2hex(random_bytes(16));
    $_SESSION['oauth_state'] = $state;
    $google = config()['google'];
    $url = 'https://accounts.google.com/o/oauth2/v2/auth?' . http_build_query([
        'client_id' => $google['client_id'],
        'redirect_uri' => $google['redirect'],
        'response_type' => 'code',
        'scope' => 'openid email profile',
        'state' => $state,
        'prompt' => 'select_account',
    ]);
    header('Location: ' . $url);
    exit;
}

function google_callback(): void
{
    $state = (string) ($_GET['state'] ?? '');
    $expected = (string) ($_SESSION['oauth_state'] ?? '');
    unset($_SESSION['oauth_state']);
    if ($expected === '' || !hash_equals($expected, $state)) {
        flash('No se pudo validar el ingreso con Google.');
        redirect('cuenta');
    }
    $code = (string) ($_GET['code'] ?? '');
    if ($code === '') {
        flash('Google no completó el ingreso.');
        redirect('cuenta');
    }
    $google = config()['google'];
    $token = http_request('POST', 'https://oauth2.googleapis.com/token', [
        'code' => $code,
        'client_id' => $google['client_id'],
        'client_secret' => $google['client_secret'],
        'redirect_uri' => $google['redirect'],
        'grant_type' => 'authorization_code',
    ]);
    $access = (string) ($token['access_token'] ?? '');
    if ($access === '') {
        flash('Google no entregó una sesión.');
        redirect('cuenta');
    }
    $info = http_request('GET', 'https://www.googleapis.com/oauth2/v3/userinfo', null, $access);
    $email = strtolower(trim((string) ($info['email'] ?? '')));
    $sub = (string) ($info['sub'] ?? '');
    if ($email === '' || $sub === '') {
        flash('Google no compartió el correo.');
        redirect('cuenta');
    }
    $name = trim((string) ($info['name'] ?? ''));
    if ($name === '') {
        $name = strstr($email, '@', true) ?: $email;
    }
    $picture = isset($info['picture']) ? (string) $info['picture'] : null;

    $stmt = db()->prepare('SELECT user_id FROM user_identities WHERE provider = ? AND provider_user_id = ?');
    $stmt->execute(['google', $sub]);
    $userId = $stmt->fetchColumn();
    if (!$userId) {
        $existing = find_user_by_email($email);
        $userId = $existing['id'] ?? create_user($email, null, $name, $picture);
        $link = db()->prepare('INSERT INTO user_identities (user_id, provider, provider_user_id) VALUES (?, ?, ?)');
        $link->execute([(int) $userId, 'google', $sub]);
        if ($existing && $picture && empty($existing['avatar_url'])) {
            $update = db()->prepare('UPDATE users SET avatar_url = ?, display_name = IF(display_name = "", ?, display_name) WHERE id = ?');
            $update->execute([$picture, $name, (int) $userId]);
        }
    }
    login_session((int) $userId);
    redirect('cuenta');
}
