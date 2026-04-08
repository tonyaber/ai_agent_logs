from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import textwrap
from app.core.config import settings


def generate_pdf_report(parsed_logs: list, ai_summary: str) -> str:
    """
    Generates a readable PDF report:
    - no horizontal clipping
    - no huge gaps
    - proper word wrapping
    - automatic page breaks
    """

    os.makedirs(settings.REPORTS_DIR, exist_ok=True)

    filename = f"weekly_report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
    path = os.path.join(settings.REPORTS_DIR, filename)

    c = canvas.Canvas(path, pagesize=letter)
    width, height = letter

    # Layout configuration
    left_margin = 40
    right_margin = 40
    top_margin = 40
    bottom_margin = 40
    usable_width = width - left_margin - right_margin

    # ===== Title =====
    c.setFont("Helvetica-Bold", 14)
    c.drawString(left_margin, height - top_margin, "Weekly Server Health Report")

    # ===== Stats =====
    c.setFont("Helvetica", 10)
    y = height - top_margin - 25

    total_logs = len(parsed_logs)
    server_errors = len([l for l in parsed_logs if l.get("status", 0) >= 500])
    client_errors = len([l for l in parsed_logs if 400 <= l.get("status", 0) < 500])

    c.drawString(left_margin, y, f"Total log entries: {total_logs}")
    y -= 12
    c.drawString(left_margin, y, f"Server errors (5xx): {server_errors}")
    y -= 12
    c.drawString(left_margin, y, f"Client errors (4xx): {client_errors}")
    y -= 18

    # ===== AI Summary Title =====
    c.setFont("Helvetica-Bold", 12)
    c.drawString(left_margin, y, "AI Analysis Summary")
    y -= 14

    # ===== Text block =====
    c.setFont("Helvetica", 10)
    text = c.beginText(left_margin, y)
    text.setLeading(12)

    # Clean markdown and excessive empty lines
    clean_summary = (
        ai_summary
        .replace("**", "")
        .replace("```", "")
    )

    # Remove multiple empty lines
    lines = [line.strip() for line in clean_summary.split("\n")]
    compact_lines = []
    previous_empty = False

    for line in lines:
        if not line:
            if not previous_empty:
                compact_lines.append("")
            previous_empty = True
        else:
            compact_lines.append(line)
            previous_empty = False

    # Approximate characters per line for Helvetica 10
    chars_per_line = int(usable_width / 6)

    for paragraph in compact_lines:
        wrapped = textwrap.wrap(paragraph, chars_per_line) if paragraph else [""]

        for line in wrapped:
            if text.getY() < bottom_margin:
                c.drawText(text)
                c.showPage()
                c.setFont("Helvetica", 10)
                text = c.beginText(left_margin, height - top_margin)
                text.setLeading(12)

            text.textLine(line)

        # Small spacing between paragraphs
        text.textLine("")

    c.drawText(text)
    c.save()

    return path

