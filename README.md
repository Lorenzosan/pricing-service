# Pricing Service Demo

Minimal pricing-service prototype using FastAPI, stateless Black-Scholes valuation, Prometheus monitoring, Docker Compose, and a clear extension path toward a gRPC or C++ pricing core.

## Purpose

This project demonstrates the engineering structure around a computational pricing service:

- validated API inputs;
- stateless pricing logic;
- observable service behavior through Prometheus metrics;
- containerized local deployment;
- unit-tested numerical code;
- clean separation between API transport and pricing computation.

The pricing model is intentionally simple. The goal is not to build a full trading platform, but to demonstrate a production-oriented service pattern for computational finance workflows.

## Architecture

```text
Client
  -> FastAPI API layer
      -> request validation
      -> market-data/input module
      -> stateless Black-Scholes pricing module
      -> metrics recording
  -> Prometheus scrapes /metrics