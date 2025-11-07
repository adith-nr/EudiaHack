"""Pricing agent placeholder logic."""
from datetime import datetime

from schema import AgentPayload


async def run_pricing(payload: AgentPayload) -> dict:
    recommendation = {
        "sku": payload.data.get("sku", "demo") if payload.data else "demo",
        "current_price": 42.0,
        "recommended_price": 39.9,
        "rationale": "Lower price to stay competitive",
    }
    return {
        "agent": "pricing",
        "received": payload.model_dump(),
        "recommendations": [recommendation],
        "generated_at": datetime.utcnow().isoformat(),
    }
