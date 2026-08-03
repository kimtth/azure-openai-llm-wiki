from __future__ import annotations

import sys
from pathlib import Path


def read_text_input(path: str | None) -> str:
    if path and path != "-":
        return Path(path).read_text(encoding="utf-8")
    if path == "-" or not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def write_text_output(text: str, path: str | None) -> None:
    if not path or path == "-":
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")
        return
    Path(path).write_text(text, encoding="utf-8")
