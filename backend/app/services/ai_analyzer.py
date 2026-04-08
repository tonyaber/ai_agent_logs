from google import genai
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def analyze_logs_ai(parsed_logs: list) -> str:
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

    Provide:
    1. Critical issues
    2. Root causes
    3. Anomalies
    4. Actionable recommendations
    """

    
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt,
    )


    return response.text.strip()
