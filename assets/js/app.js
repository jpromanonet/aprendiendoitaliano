const header = document.querySelector('.site-header');
const toggle = document.querySelector('.menu-toggle');
const backdrop = document.querySelector('.nav-backdrop');

function setMenu(open) {
  if (!header || !toggle) return;
  header.classList.toggle('menu-open', open);
  toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  if (backdrop) backdrop.hidden = !open;
  document.body.classList.toggle('nav-open', open);
}

toggle?.addEventListener('click', () => setMenu(!header.classList.contains('menu-open')));
backdrop?.addEventListener('click', () => setMenu(false));
document.querySelectorAll('.site-nav a').forEach((link) => {
  link.addEventListener('click', () => setMenu(false));
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') setMenu(false);
});
function shrinkAvatar(file) {
  return new Promise((resolve, reject) => {
    const url = URL.createObjectURL(file);
    const img = new Image();
    img.onload = () => {
      const max = 512;
      const scale = Math.min(1, max / Math.max(img.naturalWidth, img.naturalHeight));
      const width = Math.max(1, Math.round(img.naturalWidth * scale));
      const height = Math.max(1, Math.round(img.naturalHeight * scale));
      const canvas = document.createElement('canvas');
      canvas.width = width;
      canvas.height = height;
      canvas.getContext('2d')?.drawImage(img, 0, 0, width, height);
      URL.revokeObjectURL(url);
      canvas.toBlob((blob) => (blob ? resolve(blob) : reject(new Error('blob'))), 'image/jpeg', 0.86);
    };
    img.onerror = () => {
      URL.revokeObjectURL(url);
      reject(new Error('image'));
    };
    img.src = url;
  });
}

document.querySelectorAll('[data-avatar-form] input[type="file"]').forEach((input) => {
  input.addEventListener('change', async () => {
    if (input.dataset.busy === '1') return;
    const file = input.files && input.files[0];
    const form = input.form;
    if (!file || !form) return;
    input.dataset.busy = '1';
    try {
      const blob = await shrinkAvatar(file);
      const list = new DataTransfer();
      list.items.add(new File([blob], 'avatar.jpg', { type: 'image/jpeg' }));
      input.files = list.files;
    } catch (err) {
      const usable = /image\/(jpeg|png|webp)/.test(file.type) && file.size <= 8 * 1024 * 1024;
      if (!usable) {
        input.dataset.busy = '';
        input.value = '';
        window.alert('Esa foto no se pudo usar. Elegí un JPG o PNG.');
        return;
      }
    }
    form.requestSubmit();
  });
});

function fold(value) {
  return value
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[\s'"’.,!?！？。，、:：;；]/g, '');
}

document.querySelectorAll('[data-check]').forEach((button) => {
  button.addEventListener('click', () => {
    const root = button.closest('[data-exercise]');
    root?.querySelectorAll('label').forEach((label) => {
      const input = label.querySelector('input');
      const note = label.querySelector('.exercise-note');
      if (!input || !note) return;
      const value = fold(input.value.trim());
      const answer = fold(input.dataset.answer || '');
      const hint = fold(input.dataset.hint || '');
      const ok = value !== '' && (value === answer || value === hint || input.value.trim() === input.dataset.answer);
      note.textContent = ok ? 'Bien' : 'Revisala';
      note.className = 'exercise-note ' + (ok ? 'ok' : 'bad');
    });
  });
});

document.querySelectorAll('.vocab-tile').forEach((tile) => {
  tile.addEventListener('click', () => {
    const on = tile.classList.toggle('revealed');
    tile.setAttribute('aria-pressed', on ? 'true' : 'false');
  });
});

const players = [];
document.querySelectorAll('.play').forEach((button) => {
  const audio = new Audio(button.dataset.src || '');
  audio.preload = 'none';
  players.push(audio);
  const stopOthers = () => {
    players.forEach((item) => {
      if (item !== audio) item.pause();
    });
    document.querySelectorAll('audio').forEach((item) => {
      if (!item.paused) item.pause();
    });
  };
  button.addEventListener('click', () => {
    if (!audio.paused) {
      audio.pause();
      return;
    }
    stopOthers();
    audio.currentTime = 0;
    audio.play();
  });
  audio.addEventListener('play', () => button.classList.add('is-on'));
  audio.addEventListener('pause', () => button.classList.remove('is-on'));
  audio.addEventListener('ended', () => button.classList.remove('is-on'));
});

document.querySelectorAll('.audio-block audio').forEach((audio) => {
  audio.addEventListener('play', () => {
    players.forEach((item) => item.pause());
    document.querySelectorAll('.audio-block audio').forEach((item) => {
      if (item !== audio) item.pause();
    });
  });
});

const scrollKey = 'lugar:' + location.pathname;
const scrollTop = document.querySelector('.scroll-top');
let placeReady = false;

function savePlace(force) {
  if (!force && !placeReady) return;
  sessionStorage.setItem(scrollKey, String(window.scrollY));
}

function restorePlace() {
  if (location.hash) return;
  const nav = performance.getEntriesByType('navigation')[0];
  if (!nav) return;
  const cameBack = nav.type === 'reload' || nav.type === 'back_forward' || nav.redirectCount > 0;
  if (!cameBack) return;
  const y = Number(sessionStorage.getItem(scrollKey) || 0);
  if (y > 0) window.scrollTo(0, y);
}

if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
restorePlace();
window.addEventListener('load', () => {
  restorePlace();
  setTimeout(() => { placeReady = true; }, 500);
});
window.addEventListener('pageshow', restorePlace);

scrollTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
document.querySelectorAll('form').forEach((form) => {
  form.addEventListener('submit', () => savePlace(true));
});
window.addEventListener('pagehide', () => savePlace(true));
window.addEventListener('scroll', () => {
  scrollTop?.classList.toggle('is-on', window.scrollY > 480);
  savePlace(false);
}, { passive: true });
