import smtplib
from email.message import EmailMessage
from app.core.config import settings
import os

def send_report_email(pdf_path: str):
    """
    Sends the weekly health report via email.
    """

    msg = EmailMessage()
    msg["Subject"] = "Weekly Server Health Report"
    msg["From"] = settings.EMAIL_FROM
    msg["To"] = settings.EMAIL_TO

    msg.set_content(
        "Hello,\n\n"
        "Please find attached the weekly server health report.\n\n"
        "Best regards,\n"
        "AI Monitoring Agent"
    )

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(pdf_path),
        )

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(msg)