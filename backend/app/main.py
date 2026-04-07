from fastapi import FastAPI
from app.api.routes import router
from app.core.scheduler import start_scheduler
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="AI Log Analyzer",
    version="1.0.0",
)

app.include_router(router)

@app.on_event("startup")
def startup_event():
    start_scheduler()