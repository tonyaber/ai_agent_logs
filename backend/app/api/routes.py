from fastapi import APIRouter
from app.services.log_reader import read_logs
from app.services.log_parser import parse_logs
from app.services.ai_analyzer import analyze_logs_ai
from app.services.report_generator import generate_pdf_report
from app.services.notifier import send_report_email

router = APIRouter(prefix="/api")

@router.post("/generate-report")
def generate_report():
    """
    Manually triggers report generation and email delivery.
    """
    logs = read_logs()
    parsed_logs = parse_logs(logs)
    ai_summary = analyze_logs_ai(parsed_logs)
    pdf_path = generate_pdf_report(parsed_logs, ai_summary)
    send_report_email(pdf_path)

    return {
        "status": "success",
        "message": "Weekly health report generated and sent via email.",
        "report_path": pdf_path,
    }