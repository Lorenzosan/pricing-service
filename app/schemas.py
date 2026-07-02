from typing import Literal
# Literal types indicate that a variable has a specific and concrete value

from pydantic import BaseModel, Field
# BaseModel does data parsing, validation and serialization
# Field makes a new instance created for each model instance
# It enforces also sign with gt=0

class PriceRequest(BaseModel):
    spot: float = Field(..., gt=0)
    strike: float = Field(..., gt=0)
    rate: float
    volatility: float = Field(..., gt=0)
    maturity: float = Field(..., gt=0, description="Maturity in years")
    opt_typ: Literal["call", "put"]


class PriceResponse(BaseModel):
    price: float
    delta: float
    model: str
    inputs: PriceRequest


class HealthResponse(BaseModel):
    status: str
