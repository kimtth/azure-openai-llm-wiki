from __future__ import annotations

import time
from typing import Any, Dict, Iterable, Optional

import requests

DEFAULT_RETRY_STATUSES = {429, 500, 502, 503, 504}


def create_session(user_agent: Optional[str] = None) -> requests.Session:
    session = requests.Session()
    if user_agent:
        session.headers.update({"User-Agent": user_agent})
    return session


def get_json(
    session: requests.Session,
    url: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    timeout: int = 10,
    max_retries: int = 3,
    backoff: float = 1.0,
    retry_statuses: Iterable[int] = DEFAULT_RETRY_STATUSES,
    retry_after_header: bool = True,
) -> Optional[Dict[str, Any]]:
    retry_statuses_set = set(retry_statuses)

    for attempt in range(max_retries):
        try:
            response = session.get(url, params=params, timeout=timeout)
            if response.status_code in retry_statuses_set:
                if attempt < max_retries - 1:
                    wait = backoff
                    if retry_after_header and response.status_code == 429:
                        retry_after = response.headers.get("Retry-After")
                        if retry_after:
                            try:
                                wait = max(wait, float(retry_after))
                            except ValueError:
                                pass
                    time.sleep(wait)
                    backoff = min(backoff * 2, 60)
                    continue
                return None
            if response.status_code != 200:
                return None
            return response.json()
        except requests.RequestException:
            if attempt < max_retries - 1:
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)
                continue
            return None
    return None
