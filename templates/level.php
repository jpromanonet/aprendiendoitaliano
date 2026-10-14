<section class="nivel-hero">
  <div class="nivel-hero-inner">
    <p class="breadcrumb"><a href="<?= e(url()) ?>">Inicio</a> <span aria-hidden="true">/</span> <?= e($level['title']) ?></p>
    <p class="eyebrow light"><?= e($level['stage_label']) ?></p>
    <h1><?= e($level['title']) ?></h1>
    <p class="lede"><?= e($level['description']) ?></p>
    <ul class="stat-row">
      <li><strong><?= count($lessons) ?></strong> clases</li>
      <li><strong><?= number_format((int) $level['words_new'], 0, ',', '.') ?></strong> palabras nuevas</li>
    </ul>
  </div>
</section>
<div class="page-wrap">
  <div class="class-index">
    <?php foreach ($lessons as $index => $lesson): ?>
      <?php $state = $progress[(int) $lesson['id']] ?? ''; ?>
      <a class="class-link<?= $state === 'done' ? ' is-done' : ($state === 'started' ? ' is-started' : '') ?>" style="--i: <?= min((int) $index, 14) ?>" href="<?= e(url($level['slug'] . '/clase/' . $lesson['slug'])) ?>">
        <div class="class-link-top">
          <span class="class-number"><?= str_pad((string) $lesson['number'], 2, '0', STR_PAD_LEFT) ?></span>
          <span class="class-date"><?= $state === 'done' ? 'Hecha' : ($state === 'started' ? 'En curso' : e($level['title'])) ?></span>
        </div>
        <h2><?= e($lesson['title']) ?></h2>
        <p class="class-summary"><?= e($lesson['summary']) ?></p>
        <span class="class-cta"><?= $state === 'done' ? 'Repasar' : 'Entrar' ?> →</span>
      </a>
    <?php endforeach; ?>
  </div>
</div>
