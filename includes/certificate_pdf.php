<?php

declare(strict_types=1);

function certificate_pdf(array $sheet): string
{
    $pageW = 841.89;
    $pageH = 595.28;
    $green = '0 0.573 0.275';
    $red = '0.808 0.169 0.216';
    $ink = '0.024 0.208 0.141';
    $soft = '0.29 0.36 0.32';
    $ops = [];
    $ops[] = "0.992 0.984 0.965 rg 0 0 $pageW $pageH re f";
    $ops[] = "$green rg 0 0 22 $pageH re f";
    $ops[] = "$red rg " . ($pageW - 22) . " 0 22 $pageH re f";
    $ops[] = "$green RG 2.2 w 40 40 " . ($pageW - 80) . ' ' . ($pageH - 80) . ' re S';
    $ops[] = "$red RG 0.8 w 48 48 " . ($pageW - 96) . ' ' . ($pageH - 96) . ' re S';

    $flagW = 108;
    $flagH = 16;
    $flagX = ($pageW - $flagW) / 2;
    $flagY = 508;
    $stripe = $flagW / 3;
    $ops[] = "$green rg $flagX $flagY $stripe $flagH re f";
    $ops[] = "1 1 1 rg " . ($flagX + $stripe) . " $flagY $stripe $flagH re f";
    $ops[] = "$red rg " . ($flagX + $stripe * 2) . " $flagY $stripe $flagH re f";
    $ops[] = "$ink RG 0.6 w $flagX $flagY $flagW $flagH re S";

    $blocks = [
        [11, true, 1.6, $ink, 478, $sheet['kicker']],
        [36, true, 0, $ink, 430, $sheet['title']],
        [16, true, 0.4, $red, 392, $sheet['subtitle']],
        [12, false, 0, $soft, 348, $sheet['lead']],
        [26, true, 0, $ink, 308, $sheet['name']],
        [12, false, 0, $ink, 262, $sheet['body']],
        [13, true, 0.8, $red, 176, $sheet['code']],
        [11, false, 0, $soft, 150, $sheet['date']],
        [9, false, 0.3, $soft, 126, 'Sin validez oficial'],
    ];
    foreach ($blocks as [$size, $bold, $tracking, $color, $y, $text]) {
        $text = trim($text);
        if ($text === '') {
            continue;
        }
        $drawSize = $size;
        $width = pdf_text_width($text, $drawSize, $bold, $tracking);
        $max = 640;
        if ($width > $max && $width > 0) {
            $drawSize = $size * ($max / $width);
            $width = $max;
        }
        $x = ($pageW - $width) / 2;
        $font = $bold ? 'F2' : 'F1';
        $ops[] = "BT /$font $drawSize Tf $color rg $tracking Tc 1 0 0 1 $x $y Tm " . pdf_literal($text) . ' Tj ET';
    }
    $ops[] = "$red RG 0.7 w 310 292 m 532 292 l S";

    $stream = implode("\n", $ops);
    $objects = [];
    $objects[] = '<< /Type /Catalog /Pages 2 0 R >>';
    $objects[] = '<< /Type /Pages /Kids [3 0 R] /Count 1 >>';
    $objects[] = '<< /Type /Page /Parent 2 0 R /MediaBox [0 0 841.89 595.28] /Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> >>';
    $objects[] = "<< /Length " . strlen($stream) . " >>\nstream\n" . $stream . "\nendstream";
    $objects[] = '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>';
    $objects[] = '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>';

    $pdf = "%PDF-1.4\n";
    $offsets = [0];
    foreach ($objects as $i => $body) {
        $offsets[] = strlen($pdf);
        $pdf .= ($i + 1) . " 0 obj\n" . $body . "\nendobj\n";
    }
    $xref = strlen($pdf);
    $count = count($objects) + 1;
    $pdf .= "xref\n0 $count\n0000000000 65535 f \n";
    for ($i = 1; $i < $count; $i++) {
        $pdf .= sprintf("%010d 00000 n \n", $offsets[$i]);
    }
    $pdf .= "trailer\n<< /Size $count /Root 1 0 R >>\nstartxref\n$xref\n%%EOF";
    return $pdf;
}

function send_certificate_pdf(string $filename, string $pdf): void
{
    header('Content-Type: application/pdf');
    header('Content-Disposition: inline; filename="' . $filename . '"');
    header('Content-Length: ' . (string) strlen($pdf));
    echo $pdf;
    exit;
}

function pdf_literal(string $text): string
{
    $encoded = iconv('UTF-8', 'Windows-1252//TRANSLIT', $text);
    if ($encoded === false) {
        $encoded = $text;
    }
    return '(' . str_replace(['\\', '(', ')'], ['\\\\', '\\(', '\\)'], $encoded) . ')';
}

function pdf_text_width(string $text, float $size, bool $bold, float $tracking): float
{
    $encoded = iconv('UTF-8', 'Windows-1252//TRANSLIT', $text);
    if ($encoded === false) {
        $encoded = $text;
    }
    $units = 0;
    $chars = 0;
    $length = strlen($encoded);
    for ($i = 0; $i < $length; $i++) {
        $units += pdf_glyph_width(ord($encoded[$i]), $bold);
        $chars++;
    }
    $extra = $chars > 1 ? ($chars - 1) * $tracking * 1000 : 0;
    return ($units + $extra) * $size / 1000;
}

function pdf_glyph_width(int $code, bool $bold): int
{
    static $regular = [
        32 => 278, 45 => 333, 46 => 278, 47 => 278,
        48 => 556, 49 => 556, 50 => 556, 51 => 556, 52 => 556, 53 => 556, 54 => 556, 55 => 556, 56 => 556, 57 => 556,
        65 => 667, 66 => 667, 67 => 722, 68 => 722, 69 => 611, 70 => 556, 71 => 778, 72 => 722, 73 => 278, 74 => 500,
        75 => 667, 76 => 556, 77 => 833, 78 => 722, 79 => 778, 80 => 667, 81 => 778, 82 => 722, 83 => 667, 84 => 611,
        85 => 722, 86 => 667, 87 => 944, 88 => 667, 89 => 667, 90 => 611,
        97 => 556, 98 => 556, 99 => 500, 100 => 556, 101 => 556, 102 => 278, 103 => 556, 104 => 556, 105 => 222,
        106 => 222, 107 => 500, 108 => 222, 109 => 833, 110 => 556, 111 => 556, 112 => 556, 113 => 556, 114 => 333,
        115 => 500, 116 => 278, 117 => 556, 118 => 500, 119 => 722, 120 => 500, 121 => 500, 122 => 500,
        193 => 667, 201 => 611, 205 => 278, 211 => 778, 218 => 722, 220 => 722, 209 => 722,
        225 => 556, 233 => 556, 237 => 222, 243 => 556, 250 => 556, 252 => 556, 241 => 556,
    ];
    static $heavy = [
        32 => 278, 45 => 333, 46 => 278,
        48 => 556, 49 => 556, 50 => 556, 51 => 556, 52 => 556, 53 => 556, 54 => 556, 55 => 556, 56 => 556, 57 => 556,
        65 => 722, 66 => 722, 67 => 722, 68 => 722, 69 => 667, 70 => 611, 71 => 778, 72 => 722, 73 => 278, 74 => 556,
        75 => 722, 76 => 611, 77 => 833, 78 => 722, 79 => 778, 80 => 667, 81 => 778, 82 => 722, 83 => 667, 84 => 611,
        85 => 722, 86 => 667, 87 => 944, 88 => 667, 89 => 667, 90 => 611,
        97 => 556, 98 => 611, 99 => 556, 100 => 611, 101 => 556, 102 => 333, 103 => 611, 104 => 611, 105 => 278,
        106 => 278, 107 => 556, 108 => 278, 109 => 889, 110 => 611, 111 => 611, 112 => 611, 113 => 611, 114 => 389,
        115 => 556, 116 => 333, 117 => 611, 118 => 556, 119 => 778, 120 => 556, 121 => 556, 122 => 500,
        193 => 722, 201 => 667, 205 => 278, 211 => 778, 218 => 722, 220 => 722, 209 => 722,
        225 => 556, 233 => 556, 237 => 278, 243 => 611, 250 => 611, 252 => 611, 241 => 611,
    ];
    $table = $bold ? $heavy : $regular;
    return $table[$code] ?? ($bold ? 600 : 500);
}
