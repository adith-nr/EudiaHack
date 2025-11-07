"""Tiny config shim that reads directly from environment variables."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class Settings:
    env: str = field(default_factory=lambda: os.getenv("ENV", "development"))
    allowed_origins: List[str] = field(
        default_factory=lambda: [
            origin.strip()
            for origin in os.getenv("ALLOWED_ORIGINS", "*").split(",")
            if origin.strip()
        ]
    )


settings = Settings()
