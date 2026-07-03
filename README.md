# Pricing Service Demo

Minimal pricing-service prototype using FastAPI, stateless Black-Scholes valuation, Docker Compose.

## Purpose

This project demonstrates the engineering structure around a computational pricing service:

- validated API inputs;
- stateless pricing logic;
- containerized local deployment;
- unit-tested numerical code;

The pricing model is intentionally simple. The goal is not to build a full trading platform, but to demonstrate a production-oriented service pattern for computational finance workflows.

## Architecture

```text
Client
  -> FastAPI API layer
      -> request validation
      -> market-data/input module
      -> stateless Black-Scholes pricing module
      -> metrics recording