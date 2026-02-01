# Python Backend Practice

This repository documents my Python learning focused on
understanding logic and backend fundamentals — not copy-pasting solutions.

## Learning approach

All code in this repository was written manually by me.

During this process:
- I intentionally avoided using AI to generate code or logic
- I focused on designing solutions myself, even when it was slower
- I used official documentation and references (e.g. Python docs, W3Schools) to understand syntax and libraries
- AI was used only as a learning tutor — to explain concepts or verify correctness after implementation

The goal was not speed, but long-term understanding.

I believe that being able to read, reason about, and design logic independently
is essential for building reliable backend and cloud systems.

## What this repository covers
- Python fundamentals (loops, dictionaries, functions, file I/O)
- Data pipelines (validation → cleaning → aggregation)
- JSON handling and Lambda-style handlers
- Structured data processing (users, orders, CSV)
- Backend fundamentals:
  - error handling + consistent error responses
  - logging (levels, handlers, formatting)
  - typing (type hints, TypedDict, dataclasses)
  - Pydantic validation & normalization
  - testing with pytest (unit + integration tests)

## Structure
- xs_pipelines — small data-processing pipelines
- xs_data_processing — realistic user and order workflows
- xs13_serverless_idempotency — HTTP ingest (GET/POST), validation/normalization, retries/backoff, idempotent write (DynamoDB), local SAM testing
- xs14_pydantic_logging_testing_mini_service — mini “service-style” pipeline (ingest → validate with Pydantic → transform → output), structured errors, logging, and pytest tests
- mini_exercises — isolated experiments (logging, typing, pydantic, logic games)


This repository represents foundation work before moving deeper into
AWS, FastAPI, and production-grade systems.
