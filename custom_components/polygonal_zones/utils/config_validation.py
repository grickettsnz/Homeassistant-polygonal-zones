"""The config validation helpers for the polygonal zones integration."""

import os
from urllib.parse import urlparse


def are_urls_or_files(value: list[str]) -> bool:
    """Return True if any value is invalid (not a URL or file), False if all are valid."""
    return not all(is_url_or_file(item) for item in value)


def is_url_or_file(value: str) -> bool:
    """Validate that value is either a URL or valid file path."""
    try:
        result = urlparse(value)
        if all([result.scheme, result.netloc]):
            return True
    except ValueError:
        pass

    if os.path.isfile(value):
        return True

    return False
