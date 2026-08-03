from __future__ import annotations

from pathlib import Path

PathLike = str | Path


def get_repo_root(current_file: PathLike) -> Path:
    """Return the nearest ancestor containing the repository's pyproject file."""
    for parent in Path(current_file).resolve().parents:
        if (parent / "pyproject.toml").is_file():
            return parent
    return Path(current_file).resolve().parent.parent
