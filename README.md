# 🤖 AI‑Powered System Health Monitor

An AI‑assisted observability and reporting agent that automatically analyzes real production logs, detects system issues and anomalies, and sends human‑readable weekly health reports via email.

---

## ✨ Overview

This project demonstrates an **end‑to‑end AI‑assisted monitoring workflow**:

- a cloud‑deployed web service that intentionally produces errors  
- automated traffic generation to simulate real usage  
- centralized log collection  
- AI‑powered analysis  
- scheduled PDF health reports delivered by email  

The system is designed as a **headless background service**, similar to real‑world monitoring and SRE tools.

---

## 🧠 What This Agent Does

- ✅ Fetches application logs from a remote service  
- ✅ Parses and aggregates errors, warnings, and request patterns  
- ✅ Uses a Large Language Model (Gemini) as an **analysis engine**, not a chatbot  
- ✅ Detects:
  - frequent 5xx / 4xx errors  
  - unstable endpoints  
  - unusual activity patterns  
  - performance degradation signals  
- ✅ Generates a **weekly system health report (PDF)**  
- ✅ Sends the report automatically via email  
- ✅ Gracefully degrades if the AI service is temporarily unavailable  

---

## 🧩 Components

### 1️⃣ Buggy Web Application
A deliberately unstable FastAPI service deployed to the cloud.

It randomly:
- returns `500 Internal Server Error`
- emits `401 Unauthorized`
- introduces artificial latency
- writes structured logs to disk  

Used to simulate real‑world backend failures.

---

### 2️⃣ Traffic Generator
Automated traffic is generated using **GitHub Actions** on a schedule.

This ensures:
- continuous log generation  
- realistic error distribution  
- no manual interaction required  

---

### 3️⃣ AI Log Agent
The core background service that:
- fetches logs remotely  
- analyzes them  
- generates insights using an LLM  
- delivers reports automatically  

---


## 📧 Example Email Report

- Weekly system health summary  
- Error and anomaly detection  
- AI‑generated root cause analysis  
- Actionable technical recommendations  
- Delivered as a PDF attachment


A sample weekly PDF report can be downloaded here:

▶️ [https://docs/images/weekly_report_2026-04-08.png](https://github.com/tonyaber/ai_agent_logs/blob/main/docs/reports/weekly_report_2026-04-08.pdf)

---

## 🛡 Resilience by Design

This system is intentionally built to handle real production conditions:

- ✅ Retry logic with exponential backoff for AI calls  
- ✅ Graceful fallback when LLM services are unavailable  
- ✅ Email delivery continues even during partial AI outages  
- ✅ Clear separation of concerns between ingestion, analysis and reporting  

> “The system remains operational and informative even when external AI services experience downtime.”

---

## 🚀 Why This Project Is Interesting

This is **not a chatbot**.

It demonstrates:
- AI used as an **engineering tool**, not a UI feature  
- observability and SRE principles  
- real failure simulation  
- backend‑only design (no UI required)  
- production‑style error handling  
- cloud‑native thinking  

---

## 🧩 Tech Stack

- Python 3  
- FastAPI  
- Google Gemini (LLM API)  
- GitHub Actions  
- SMTP Email Delivery  
- Render (cloud deployment)  
- PDF generation  
- Linux‑style logging  

---

## 🔮 Possible Extensions

- Authentication for log endpoints  
- Prometheus / Loki integration  
- Multi‑service log analysis  
- Incident severity scoring  
- Alerting thresholds  
- Web dashboard for report history  

---

## 🧑‍💻 Author Notes

This project was built as a demonstration of **AI‑assisted system observability**
and **production‑grade backend decision making**.

It intentionally embraces:
- partial failures  
- external service instability  
- realistic monitoring workflows  

---

## ✅ Status

- 🟢 Fully working end‑to‑end  
- 🟢 Actively maintained  
- 🟢 Ready for demo, portfolio and interview discussion  
