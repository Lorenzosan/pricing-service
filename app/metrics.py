from prometheus_client import Counter, Gauge, Histogram


PRICE_REQUESTS_TOTAL = Counter(
    "pricing_requests_total",
    "Total number of pricing requests",
    ["option_type"],
)

PRICE_ERRORS_TOTAL = Counter(
    "pricing_errors_total",
    "Total number of pricing errors",
)

PRICE_REQUEST_LATENCY_SECONDS = Histogram(
    "pricing_request_latency_seconds",
    "Latency of pricing requests in seconds",
)

LAST_PRICE_VALUE = Gauge(
    "last_price_value",
    "Last computed option price",
)
