import time

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.black_scholes import price_bs
from app.data_provider import get_market_snapshot
from app.metrics import (
    LAST_PRICE_VALUE,
    PRICE_ERRORS_TOTAL,
    PRICE_REQUEST_LATENCY_SECONDS,
    PRICE_REQUESTS_TOTAL,
)
from app.schemas import HealthResponse, PriceRequest, PriceResponse


app = FastAPI(
    title="Pricing Service Demo",
    description="Minimal pricing service with Black-Scholes valuation and Prometheus metrics.",
    version="0.1.0",
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post("/price", response_model=PriceResponse)
def price_option(request: PriceRequest) -> PriceResponse:
    start_time = time.perf_counter()

    try:
        get_market_snapshot()

        result = price_bs(
            spot=request.spot,
            strike=request.strike,
            rate=request.rate,
            volatility=request.volatility,
            maturity=request.maturity,
            opt_typ=request.option_type,
        )

        PRICE_REQUESTS_TOTAL.labels(option_type=request.option_type).inc()
        LAST_PRICE_VALUE.set(result.price)

        return PriceResponse(
            price=result.price,
            delta=result.delta,
            model="black_scholes",
            inputs=request,
        )

    except Exception:
        PRICE_ERRORS_TOTAL.inc()
        raise

    finally:
        elapsed = time.perf_counter() - start_time
        PRICE_REQUEST_LATENCY_SECONDS.observe(elapsed)


@app.get("/metrics")
def metrics() -> Response:
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
