import requests
from app.core.config import settings


def read_logs():
    """
    Fetch logs from buggy_app via HTTP.
    """
    response = requests.get(settings.LOG_SOURCE_URL, timeout=10)
    return response.json()
