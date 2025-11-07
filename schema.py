"""Pydantic models shared between Express and FastAPI layers."""
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AgentRole(str, Enum):
    coordinator = "coordinator"
    pricing = "pricing"
    analytics = "analytics"
    finance = "finance"
    insight = "insight"


class AgentContext(BaseModel):
    store_id: str = Field(..., description="Shopify store identifier")
    currency: str = Field(..., min_length=3, max_length=3, description="ISO currency code")


class AgentPayload(BaseModel):
    role: AgentRole
    context: AgentContext
    goals: List[str]
    data: Optional[Dict[str, Any]] = None


class PricingRecommendation(BaseModel):
    sku: str
    current_price: float
    recommended_price: float
    rationale: str


class AnalyticsSummary(BaseModel):
    store_id: str
    timeframe: str
    metrics: Dict[str, Any]
