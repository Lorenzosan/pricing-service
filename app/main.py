from fastapi import FastAPI

from app.black_scholes import price_bs
from app.schemas import HealthResponse, PriceRequest, PriceResponse


app = FastAPI(
    title="Pricing Service Demo",
    description="Minimal pricing service with Black-Scholes valuation.",
    version="0.1.0",
)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post("/price", response_model=PriceResponse)
def price_option(request: PriceRequest) -> PriceResponse:
    result = price_bs(
        spot=request.spot,
        strike=request.strike,
        rate=request.rate,
        volatility=request.volatility,
        maturity=request.maturity,
        option_type=request.option_type,
    )

    return PriceResponse(
        price=result.price,
        delta=result.delta,
        model="black_scholes",
        inputs=request,
    )
