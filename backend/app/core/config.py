import os

class Settings:
    LOG_PATH = "logs/server.log"
    REPORTS_DIR = "reports/"

    # Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    # Scheduler
    SCHEDULE_DAY = "mon"
    SCHEDULE_TIME = "08:00"

    # Email
    SMTP_HOST = os.getenv("SMTP_HOST")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

    EMAIL_FROM = os.getenv("EMAIL_FROM")
    EMAIL_TO = os.getenv("EMAIL_TO")

settings = Settings()