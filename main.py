"""FastAPI entry point that wires routes to agent placeholders."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents import analytics, coordinator, finance, health, insight, pricing
from config import settings
from logger import logger
from schema import AgentPayload

app = FastAPI(title="Shopify Agentic LLM Service", version="0.1.0")


class AnalyticsJob(BaseModel):
    topic: str
    payload: dict | None = None


class PayoutsPayload(BaseModel):
    payouts: list[dict] | None = None


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return await health.service_status()


@app.post("/coordinator/run")
async def run_coordinator(payload: AgentPayload):
    return await coordinator.run_coordinator(payload)


@app.post("/pricing/run")
async def run_pricing(payload: AgentPayload):
    return await pricing.run_pricing(payload)


@app.post("/analytics/enqueue")
async def enqueue_analytics(job: AnalyticsJob):
    return await analytics.enqueue_job(job.topic)


@app.get("/analytics/insights")
async def analytics_insights():
    return await analytics.fetch_insights()


@app.get("/finance/snapshot")
async def finance_snapshot():
    return await finance.snapshot()


@app.post("/finance/payouts/reconcile")
async def finance_reconcile(payload: PayoutsPayload):
    return await finance.reconcile(payload.payouts)


@app.get("/insight/summary")
async def insight_summary():
    return await insight.summary()


@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI layer started", extra={"env": settings.env})


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("FastAPI layer stopped")
