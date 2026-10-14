"""Genera MP3 de las palabras y frases que el sitio deja escuchar."""

import asyncio
import hashlib
import json
import sys
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "audio"
VOICE = "it-IT-ElsaNeural"
RATE = "-8%"


def audio_id(text: str, pinyin: str = "") -> str:
    key = text.strip()
    if pinyin.strip():
        key += "\n" + pinyin.strip()
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


def speak_of(text: str, pinyin: str = "") -> str:
    return text.strip()


def collect() -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    seen: set[str] = set()

    def add(text: str, pinyin: str = "") -> None:
        text = (text or "").strip()
        pinyin = (pinyin or "").strip()
        if not text:
            return
        ident = audio_id(text, pinyin)
        if ident in seen:
            return
        seen.add(ident)
        items.append((text, pinyin))

    lexicon = json.loads((ROOT / "data" / "lexicon.json").read_text(encoding="utf-8"))
    for row in lexicon:
        add(row["hanzi"], row["pinyin"])
        add(row.get("ex_zh") or "")
    for name in ("a1.json", "a2.json", "b1.json", "b2.json", "c1.json", "c2.json"):
        lessons = json.loads((ROOT / "data" / name).read_text(encoding="utf-8"))
        for lesson in lessons:
            for extra in lesson.get("extras") or []:
                add(extra.get("hanzi") or "", extra.get("pinyin") or "")
            for line in lesson.get("dialogue") or []:
                add(line.get("zh") or "")
    return items


async def synth(text: str, dest: Path, sem: asyncio.Semaphore) -> str:
    if dest.exists() and dest.stat().st_size > 800:
        return "skip"
    last = "error"
    async with sem:
        for attempt in range(5):
            try:
                communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
                tmp = dest.with_suffix(".part")
                await communicate.save(str(tmp))
                if tmp.stat().st_size > 800:
                    tmp.replace(dest)
                    return "ok"
                tmp.unlink(missing_ok=True)
                last = "corto"
            except Exception as exc:
                last = str(exc)
                await asyncio.sleep(1.2 * (attempt + 1))
    print("FALLO", text, last, file=sys.stderr)
    return "fail"


async def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    items = collect()
    print(f"piezas {len(items)}", flush=True)
    sem = asyncio.Semaphore(6)
    done = 0
    failed = 0

    async def one(text: str, pinyin: str) -> None:
        nonlocal done, failed
        dest = OUT / f"{audio_id(text, pinyin)}.mp3"
        status = await synth(speak_of(text, pinyin), dest, sem)
        done += 1
        if status == "fail":
            failed += 1
        if done % 100 == 0 or done == len(items):
            print(f"{done}/{len(items)} fallos {failed}", flush=True)

    await asyncio.gather(*(one(text, pinyin) for text, pinyin in items))
    print(f"listo {done} fallos {failed}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
