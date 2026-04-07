from apscheduler.schedulers.background import BackgroundScheduler
from app.services.log_reader import read_logs
from app.services.log_parser import parse_logs
from app.services.ai_analyzer import analyze_logs_ai
from app.services.report_generator import generate_pdf_report
from app.services.notifier import send_report_email
from app.core.config import settings

def weekly_job():
    """
    Weekly scheduled job:
    - Read logs
    - Analyze them
    - Generate PDF report
    - Send report via email
    """
    logs = read_logs()
    parsed_logs = parse_logs(logs)
    ai_summary = analyze_logs_ai(parsed_logs)
    pdf_path = generate_pdf_report(parsed_logs, ai_summary)
    send_report_email(pdf_path)

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        weekly_job,
        trigger="cron",
        day_of_week=settings.SCHEDULE_DAY,
        hour=int(settings.SCHEDULE_TIME.split(":")[0]),
        minute=int(settings.SCHEDULE_TIME.split(":")[1]),
    )
    scheduler.start()