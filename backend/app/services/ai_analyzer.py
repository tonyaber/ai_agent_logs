from google import genai
from app.core.config import settings
import time

client = genai.Client(api_key=settings.GEMINI_API_KEY)

MODELS = ["models/gemini-2.0-flash", "models/gemini-2.5-pro"]


def analyze_logs_ai(parsed_logs: list) -> str:
    
    error_logs = [
        f"[{l['timestamp']}] {l['level']} {l['message']}"
        for l in parsed_logs
        if l["status"] >= 400
    ]
    print("error_logs: ", error_logs)
    prompt = f"""
        You are a senior backend and SRE engineer.

        You are analyzing real production application logs.

        Below is a list of log entries containing warnings and errors.
        Each entry includes a timestamp, severity level, and message.

        Logs:
        {"\n".join(error_logs)}

        Your task:
        1. Identify recurring error patterns or themes.
        2. Group similar errors together and explain what they indicate.
        3. Infer likely root causes based on the log messages.
        4. Detect possible security or stability risks.
        5. Assess the overall severity and urgency of the issues.
        6. Provide clear, actionable technical recommendations to improve system reliability.

        Important:
        - Base your analysis only on the log messages above.
        - Do not assume missing context.
        - Focus on engineering and operational insights.
        - Keep the response concise, structured, and production-oriented.
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

