import google.generativeai as genai
from app.core.config import settings

# Configure Gemini
genai.configure(api_key=settings.GEMINI_API_KEY)

# You can switch models if needed:
# gemini-1.5-pro (strong reasoning)
# gemini-1.5-flash (faster, cheaper)
model = genai.GenerativeModel("gemini-1.5-pro")


def analyze_logs_ai(parsed_logs: list) -> str:
    """
    Uses Google Gemini to analyze parsed server logs
    and generate a technical weekly summary.
    """

    total_requests = len(parsed_logs)
    server_errors = len([l for l in parsed_logs if l["status"] >= 500])
    client_errors = len([l for l in parsed_logs if 400 <= l["status"] < 500])

    prompt = f"""
You are a senior backend engineer.

Analyze the following server log statistics and produce
a concise weekly infrastructure health report.

Statistics:
- Total requests: {total_requests}
- Server errors (5xx): {server_errors}
- Client errors (4xx): {client_errors}

Please provide:
1. Most critical issues.
2. Possible root causes.
3. Detected anomalies or spikes.
4. Clear, actionable recommendations.

Keep the response short, technical, and production-oriented.
"""

    response = model.generate_content(prompt)

    return response.text.strip()