import os
from dotenv import load_dotenv
from pathlib import Path

# 👇 EXPLICIT path to backend/.env
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    LOG_SOURCE_URL = os.getenv("LOG_SOURCE_URL")
    REPORTS_DIR = "reports/"
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    EMAIL_FROM = os.getenv("EMAIL_FROM")
    EMAIL_TO = os.getenv("EMAIL_TO")
    SCHEDULE_DAY = "mon"
    SCHEDULE_TIME = "08:00"

settings = Settings()
