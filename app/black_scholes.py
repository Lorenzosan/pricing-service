# This import provides functions for adding special methods
# like __init__() and __repr()__
from dataclasses import dataclass

# For functions like the logarithm or erf
import math


# frozen == True makes it throw an exception if fields are assigned
# used to replicate "immutability"
@dataclass(frozen=True)
class OptionResult:
    price: float
    delta: float

def normal_cdf(x: float) -> float:
    return 0.5 * (1.0 * math.erf(x/math.sqrt(2.0)))

def price_bs(
        spot: float,
        strike: float,
        rate: float,
        volatility: float,
        maturity: float,
        opt_typ: str,
        ) -> OptionResult:

    if spot <= 0:
        raise ValueError("Spot must be positive")
    if strike <= 0:
        raise ValueError("Strike must be positive")
    if volatility <= 0:
        raise ValueError("Volatility must be positive")
    if maturity <= 0:
        raise ValueError("Maturity must be positive")
    if opt_typ not in {"put", "call"}:
        raise ValueError("Option type must be call or put")
    
    sqrt_t = math.sqrt(maturity)

    d1 = (math.log(spot/strike) +
          (rate + 0.5*volatility*volatility) * maturity
          ) / (volatility * sqrt_t)

    d2 = d1 - volatility * sqrt_t

    discounted_strike = strike * math.exp(-rate * maturity)
    
    if opt_typ == "call":
        price  = spot * normal_cdf(d1) - discounted_strike * normal_cdf(d2)
        delta  = normal_cdf(d1)
    else:
        price  = discounted_strike * normal_cdf(-d2) - spot * normal_cdf(-d1)
        delta  = normal_cdf(d1) - 1

    return OptionResult(price=price, delta=delta)
