# Aprendiendo italiano

Curso de italiano para hispanohablantes, de A1 a C2. Clases, audios, diccionario, libros y certificados. La interfaz sigue el mismo recorrido del template: tres etapas, práctica escrita y autoevaluación.

Los libros se cargan después en `storage/libros/`.

## Puesta en marcha

1. Copiá `config.example.php` a `config.php` y completá la base.
2. Visitá `/aprendiendoitaliano/index.php/instalar?key=LA_SEED_KEY`.
3. Generá los audios con `python scripts/generate_audio.py` (voz `it-IT-ElsaNeural`).

El léxico y las clases del A1 salen de `python scripts/build_italiano.py`.
