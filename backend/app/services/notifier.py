import smtplib
import ssl
from email.message import EmailMessage
from app.core.config import settings
import os


def send_report_email(pdf_path: str):
    if not settings.SMTP_HOST:
        raise RuntimeError("SMTP_HOST is not set")
    if not settings.SMTP_USER:
        raise RuntimeError("SMTP_USER is not set")
    if not settings.SMTP_PASSWORD:
        raise RuntimeError("SMTP_PASSWORD is not set")

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

    context = ssl.create_default_context()

    # ✅ THIS IS THE IMPORTANT PART
    with smtplib.SMTP_SSL(settings.SMTP_HOST, 465, context=context) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.send_message(msg)
