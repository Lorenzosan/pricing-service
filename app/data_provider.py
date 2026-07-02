from dataclasses import dataclass


@dataclass(frozen=True)
class MarketSnapshot:
    source: str
    timestamp: str | None = None


def get_market_snapshot() -> MarketSnapshot:
    return MarketSnapshot(source="request_payload")
