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

