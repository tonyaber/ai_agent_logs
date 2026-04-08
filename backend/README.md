🤖 AI‑Powered System Health Monitor
An AI‑assisted observability and reporting agent that automatically analyzes real production logs, detects issues and anomalies, and delivers human‑readable weekly system health reports via email.

✨ Overview
This project demonstrates an end‑to‑end AI‑assisted monitoring workflow:

a cloud‑deployed web service that intentionally produces errors
automated traffic generation to simulate real usage
centralized log analysis
LLM‑powered insights
scheduled PDF health reports delivered by email

The system is designed as a headless background service, similar to real-world monitoring and SRE tools.

🧠 What This Agent Does
✅ Fetches application logs from a remote service
✅ Parses and aggregates errors, warnings, and request patterns
✅ Uses a Large Language Model (Gemini) as an analysis engine, not a chatbot
✅ Detects:

frequent 5xx / 4xx errors
unstable endpoints
unusual activity patterns
performance degradation signals
✅ Generates a weekly system health report (PDF)
✅ Sends the report automatically via email
✅ Degrades gracefully if the AI service is temporarily unavailable


🏗 Architecture
┌────────────────────────────┐
│      GitHub Actions        │
│  (scheduled traffic)       │
└──────────────┬─────────────┘
               │
               ▼
┌────────────────────────────┐
│        Buggy Web App        │
│   (FastAPI, deployed)      │
│                            │
│  • 200 / 401 / 500 errors  │
│  • latency spikes          │
│  • structured logging      │
└──────────────┬─────────────┘
               │
               ▼
        /internal/logs
               │
               ▼
┌────────────────────────────┐
│        AI Log Agent         │
│   (FastAPI background svc) │
│                            │
│  • fetch logs via HTTP     │
│  • parse & aggregate       │
│  • Gemini AI analysis      │
│  • fallback logic          │
│  • PDF generation          │
│  • email delivery          │
└────────────────────────────┘


📦 Components
1️⃣ Buggy Web Application
A deliberately unstable FastAPI service deployed to the cloud.
It randomly:

returns 500 Internal Server Error
emits 401 Unauthorized
introduces artificial latency
writes structured logs to disk

Used to simulate real‑world backend failures.

2️⃣ Traffic Generator
Automated traffic is generated using GitHub Actions on a schedule.
This ensures:

continuous log generation
realistic error distribution
no manual interaction required


3️⃣ AI Log Agent
The core system health agent that:

fetches logs remotely
analyzes them
generates insights using an LLM
delivers reports automatically


🧪 Example AI‑Generated Insights

Frequent server errors (5xx) were detected on the /sometimes-fails endpoint, indicating instability in backend dependencies.
Repeated unauthorized access attempts on /auth suggest missing authentication guards or external probing.
Occasional latency spikes indicate blocking operations during request handling.
Recommendation: stabilize error-prone endpoints, add proper authentication middleware, and instrument latency monitoring.


📧 Example Email Report

Subject: Weekly Server Health Report

Total requests analyzed
Server error trends
Client error patterns
AI‑generated root cause analysis
Actionable recommendations


📎 Delivered as a structured PDF attachment.

🖼 Example Email Preview

Place your screenshot or GIF here

Plain Text📸 Example:- PDF health report opened from email- AI analysis summary- Weekly error trendsПоказати більше рядків
(Add screenshots in /docs/images/ and reference them here)

🛡 Resilience by Design
