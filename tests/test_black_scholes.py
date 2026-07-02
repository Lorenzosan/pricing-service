import math

import pytest

from app.black_scholes import price_black_scholes


def test_call_price_is_positive() -> None:
    result = price_black_scholes(
        spot=100.0,
        strike=100.0,
        rate=0.03,
        volatility=0.20,
        maturity=1.0,
        option_type="call",
    )

    assert result.price > 0.0
    assert 0.0 < result.delta < 1.0


def test_put_price_is_positive() -> None:
    result = price_black_scholes(
        spot=100.0,
        strike=100.0,
        rate=0.03,
        volatility=0.20,
        maturity=1.0,
        option_type="put",
    )

    assert result.price > 0.0
    assert -1.0 < result.delta < 0.0


def test_call_put_parity() -> None:
    spot = 100.0
    strike = 105.0
    rate = 0.03
    volatility = 0.20
    maturity = 1.0

    call = price_black_scholes(
        spot=spot,
        strike=strike,
        rate=rate,
        volatility=volatility,
        maturity=maturity,
        option_type="call",
    )

    put = price_black_scholes(
        spot=spot,
        strike=strike,
        rate=rate,
        volatility=volatility,
        maturity=maturity,
        option_type="put",
    )

    lhs = call.price - put.price
    rhs = spot - strike * math.exp(-rate * maturity)

    assert lhs == pytest.approx(rhs, rel=1e-10)


def test_invalid_option_type_raises() -> None:
    with pytest.raises(ValueError):
        price_black_scholes(
            spot=100.0,
            strike=100.0,
            rate=0.03,
            volatility=0.20,
            maturity=1.0,
            option_type="invalid",
        )
