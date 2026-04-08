from google import genai
from app.core.config import settings
import time

client = genai.Client(api_key=settings.GEMINI_API_KEY)

MODELS = ["models/gemini-2.5-flash", "models/gemini-2.5-pro"]


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

    for model in MODELS:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                print(f"Using model: {model}")
                return response.text.strip()

            except Exception as e:
                if "503" in str(e):
                    time.sleep(1.5 * (attempt + 1))  # backoff
                    continue
                break
        
    return "AI temporarily unavailable"

