from app.core.config import settings

def read_logs():
    try:
        with open(settings.LOG_PATH, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return []