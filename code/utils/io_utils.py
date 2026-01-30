from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional


def read_text_input(path: Optional[str]) -> str:
    if path and path != "-":
        return Path(path).read_text(encoding="utf-8")
    if path == "-" or not sys.stdin.isatty():
        return sys.stdin.read()
    return ""


def write_text_output(text: str, path: Optional[str]) -> None:
    if not path or path == "-":
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")
        return
    Path(path).write_text(text, encoding="utf-8")
