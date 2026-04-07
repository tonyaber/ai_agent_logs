from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from app.core.config import settings
from datetime import datetime
import os

def generate_pdf_report(parsed_logs: list, ai_summary: str) -> str:
    """
    Generates a PDF weekly server health report.
    """

    filename = f"weekly_report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
    path = os.path.join(settings.REPORTS_DIR, filename)

    c = canvas.Canvas(path, pagesize=letter)

    c.drawString(50, 750, "Weekly Server Health Report")
    c.drawString(50, 730, f"Total log entries: {len(parsed_logs)}")

    server_errors = len([l for l in parsed_logs if l["status"] >= 500])
    client_errors = len([l for l in parsed_logs if 400 <= l["status"] < 500])

    c.drawString(50, 710, f"Server errors (5xx): {server_errors}")
    c.drawString(50, 690, f"Client errors (4xx): {client_errors}")

    c.drawString(50, 650, "AI Analysis Summary:")
    y = 630

    for line in ai_summary.split("\n"):
        c.drawString(50, y, line[:95])
        y -= 14

    c.save()
    return path