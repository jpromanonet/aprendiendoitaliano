<?php

declare(strict_types=1);

return [
    'base_path' => '/aprendiendoitaliano',
    'app_url' => 'http://127.0.0.1/aprendiendoitaliano',
    'db' => [
        'host' => '127.0.0.1',
        'port' => 3306,
        'name' => 'aprendiendoitaliano',
        'user' => 'root',
        'pass' => '',
        'charset' => 'utf8mb4',
    ],
    'google' => [
        'client_id' => '',
        'client_secret' => '',
        'redirect' => 'http://127.0.0.1/aprendiendoitaliano/index.php/auth/google/callback',
    ],
    'seed_key' => 'change-me',
];
