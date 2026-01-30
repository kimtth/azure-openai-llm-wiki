from __future__ import annotations

import re

GITHUB_REPO_URL_PATTERN = re.compile(r"\(https://github\.com/([^/\s]+)/([^/\s)]+)\)")
GITHUB_REPO_URL_WITH_COLON_PATTERN = re.compile(r"\(https://github\.com/([^/\s]+)/([^/\s)]+)\):?\s*")
GITHUB_BADGE_PATTERN = re.compile(r"img\.shields\.io/github/stars/([^/]+)/([^/?\s]+)")
DATE_TOKEN_PATTERN = re.compile(r"\[([A-Z][a-z]{2} \d{4})\]")


def clean_repo_name(repo: str) -> str:
    return repo.rstrip(").")
