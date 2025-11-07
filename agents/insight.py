"""Insight agent placeholder logic."""
from datetime import datetime


async def summary() -> dict:
    return {
        "agent": "insight",
        "summary": ["Competitor A dropped 5%", "Consider bundle discount"],
        "generated_at": datetime.utcnow().isoformat(),
    }
