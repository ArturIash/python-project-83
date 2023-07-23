import validators
from urllib.parse import urlparse

MAX_URL_LEN = 255


def normalize_url(url: str) -> str:
    parsed_url = urlparse(url, allow_fragments=True)
    return f"{parsed_url.scheme}://{parsed_url.netloc}"
