from __future__ import annotations

from pathlib import Path
from typing import Union


PathLike = Union[str, Path]


def get_repo_root(current_file: PathLike) -> Path:
    return Path(current_file).resolve().parent.parent
