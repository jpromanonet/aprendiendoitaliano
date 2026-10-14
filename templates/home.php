<section class="home-hero">
  <div class="home-hero-media" aria-hidden="true">
    <img class="home-hero-img" src="<?= e(url('assets/flag.svg')) ?>" alt="">
  </div>
  <div class="home-hero-scrim" aria-hidden="true"></div>
  <div class="home-hero-inner">
    <p class="eyebrow light">Italiano</p>
    <h1 class="home-hero-brand"><span class="hero-es">Aprendiendo</span><span class="hero-lang">Italiano</span></h1>
    <p class="home-hero-line">Clases, audios y un diccionario con las palabras de A1 a C2.</p>
    <div class="home-hero-actions">
      <a class="primary-btn" href="#clases">Ver clases</a>
    </div>
  </div>
</section>

<div class="home-direct">
  <section class="how-strip" aria-label="Cómo usar el sitio">
    <?php
    $steps = [
        ['01', 'Elegí un nivel', 'El A1 es el punto de partida.'],
        ['02', 'Leé y escuchá', 'Cada palabra y cada frase tiene su audio.'],
        ['03', 'Practicá', 'Escribí en italiano y hacé la autoevaluación.'],
        ['04', 'Buscá', 'El diccionario cubre de A1 a C2.'],
    ];
    foreach ($steps as $index => [$step, $stepTitle, $stepBody]): ?>
      <article style="--i: <?= $index ?>">
        <span><?= e($step) ?></span>
        <strong><?= e($stepTitle) ?></strong>
        <p><?= e($stepBody) ?></p>
      </article>
    <?php endforeach; ?>
  </section>

  <section class="system" id="sistema">
    <p class="eyebrow">El sistema</p>
    <h2>Seis niveles, tres etapas</h2>
    <p class="lede">El italiano se ordena con el QCER, el Quadro Comune Europeo di Riferimento: seis niveles y tres etapas. A1 y A2 son la etapa inicial. B1 y B2, la media. C1 y C2, la avanzada. En cada nivel hay clases con audio, práctica y una autoevaluación. Se cursan en ese orden.</p>
    <p class="cert-note">Al completar todas las clases de un nivel, el certificado queda en Certificados. No tiene validez oficial: solo deja constancia de que terminaste ese nivel acá.</p>
    <div class="stage-grid">
      <article>
        <p class="stage-kicker">01</p>
        <h3>Etapa inicial</h3>
        <p>A1 y A2. Saludos, casa, trabajo y el pasado reciente.</p>
      </article>
      <article>
        <p class="stage-kicker">02</p>
        <h3>Etapa media</h3>
        <p>B1 y B2. Opinión, viaje y argumento.</p>
      </article>
      <article>
        <p class="stage-kicker">03</p>
        <h3>Etapa avanzada</h3>
        <p>C1 y C2. Precisión, registro y matiz.</p>
      </article>
    </div>
  </section>

  <section class="home-classes" id="clases">
    <div class="home-classes-head">
      <div>
        <p class="eyebrow">Recorrido</p>
        <h2>De A1 a C2</h2>
      </div>
    </div>
    <?php
    $grouped = [];
    foreach ($levels as $level) {
        $grouped[$level['stage_label']][] = $level;
    }
    foreach ($grouped as $label => $items): ?>
      <div class="level-cut level-board">
        <div class="level-cut-head">
          <div>
            <p class="level-cut-label">Etapa</p>
            <h3><?= e($label) ?></h3>
          </div>
        </div>
        <div class="level-grid">
          <?php foreach ($items as $level): ?>
            <a class="level-card" href="<?= e(url($level['slug'])) ?>">
              <span class="level-card-kicker"><?= e($level['title']) ?></span>
              <strong><?= (int) ($lessonCounts[(int) $level['id']] ?? 0) ?> clases</strong>
              <p><?= e($level['description']) ?></p>
              <em><?= number_format((int) $level['words_new'], 0, ',', '.') ?> palabras nuevas</em>
              <span class="class-cta">Abrir nivel →</span>
            </a>
          <?php endforeach; ?>
        </div>
      </div>
    <?php endforeach; ?>
  </section>
</div>
