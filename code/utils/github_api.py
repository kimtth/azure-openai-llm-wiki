from __future__ import annotations

from datetime import datetime
from typing import Optional

from .http_utils import create_session, get_json

DEFAULT_GITHUB_API = "https://api.github.com/repos/{owner}/{repo}"
DEFAULT_USER_AGENT = "awesome-azure-openai-llm/1.0"


def fetch_repo_data(
    owner: str,
    repo: str,
    *,
    session=None,
    timeout: int = 10,
    max_retries: int = 3,
) -> Optional[dict]:
    if session is None:
        session = create_session(DEFAULT_USER_AGENT)
    url = DEFAULT_GITHUB_API.format(owner=owner, repo=repo)
    return get_json(session, url, timeout=timeout, max_retries=max_retries)


def get_repo_created_date(
    owner: str,
    repo: str,
    *,
    session=None,
    timeout: int = 10,
    max_retries: int = 3,
) -> Optional[str]:
    data = fetch_repo_data(owner, repo, session=session, timeout=timeout, max_retries=max_retries)
    if not data:
        return None
    created_at = data.get("created_at")
    if not created_at:
        return None
    dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    return f"[{dt.strftime('%b %Y')}]"


def get_repo_description(
    owner: str,
    repo: str,
    *,
    session=None,
    timeout: int = 10,
    max_retries: int = 3,
) -> Optional[str]:
    data = fetch_repo_data(owner, repo, session=session, timeout=timeout, max_retries=max_retries)
    if not data:
        return None

    description = data.get("description")
    if not description:
        topics = data.get("topics", [])
        if topics:
            return f"Repository for {', '.join(topics)}"
        return None

    description = description.strip()
    if len(description) > 150:
        description = description[:150].rsplit(" ", 1)[0] + "."
    return description
