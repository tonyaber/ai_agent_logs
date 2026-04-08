import requests
from app.core.config import settings


def read_logs():
    """
    Fetch logs from buggy_app via HTTP.
    """
    response = requests.get(settings.LOG_PATH, timeout=10)
    response.raise_for_status()
    return response.text.splitlines()
