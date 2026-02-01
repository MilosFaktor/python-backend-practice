# XS14 — Mini Backend Service Pipeline

XS14 is a mini service-style backend pipeline implemented in pure Python.

The goal of this exercise is to understand how backend systems process data internally —
from ingestion, through validation and transformation, to structured output —
without relying on frameworks or cloud services.

This project focuses on backend fundamentals and system design principles,
not speed or shortcuts.

---

## Purpose

XS14 was built to practice designing a structured backend pipeline
that can be packaged, deployed, and executed consistently using Docker.

Docker is used to ensure consistent execution regardless of local Python versions or host environments.

The focus is on:
- clean pipeline boundaries (ingest → validate → transform → output)
- strong data contracts with **Pydantic**
- predictable error responses
- **logging and observability** (request_id, step logs, execution time)
- **testing** (unit + integration)

The intention is that the internal architecture remains stable while the execution environment changes
(local execution → containerized execution).

Only the runtime changes — the pipeline logic does not.

XS14 is intentionally implemented as a single-run execution pipeline (similar to a batch job or Lambda-style invocation).
It is not an HTTP API or long-running service.
This keeps the focus on backend data flow, contracts, and reliability rather than networking concerns.



---

## High-level flow

JSON input
  ↓
Ingest layer
  ↓
Validation layer (Pydantic)
  ↓
Transformation layer
  ↓
Output builder
  ↓
Structured response

Each stage has a single responsibility and can fail safely.

---

## Why this structure is extensible

This project is intentionally modular:

- **Ingest** can change (file → HTTP → S3) without touching validation or business logic
- **Validation** enforces a stable contract regardless of input source
- **Transform** stays pure and testable
- **Output** guarantees a consistent response shape
- **Logging + tests** provide safety as the pipeline grows

This is the same design logic used in production systems — only the adapters change.


## Features

- pipeline architecture with clear responsibilities per module
- strict schema validation with **Pydantic v2** (`extra="forbid"`)
- input normalization (id parsing, active parsing, whitespace stripping)
- unified error model (`ErrorInfo`) and deterministic error responses
- structured logging (levels, request_id, execution timing)
- centralized configuration (`config.py`)
- pytest test suite (unit + full pipeline integration)


## Configuration
The pipeline behavior is controlled using environment variables.

- MODE
  - ok → processes sample_ok.json (default)
  - bad → processes sample_bad.json

---

## Project structure
```bash
xs14/
├── README.md
├── commands.sh
├── data
│   ├── sample_bad.json
│   └── sample_ok.json
├── requirements.txt
├── src
│   └── xs14
│       ├── __init__.py
│       ├── config.py           # centralized settings
│       ├── errors.py           # unified error structure
│       ├── ingest.py           # input ingestion & IO errors
│       ├── logging_setup.py    # logging configuration
│       ├── main.py             # orchestrator
│       ├── models.py           # Pydantic models
│       ├── output.py           # response builders
│       ├── transform.py        # business logic
│       ├── utils
│       │   ├── __init__.py
│       │   └── util.py         # execution timing
│       └── validate.py         # schema validation
└── tests
    ├── test_integration_flow.py
    ├── test_output.py
    ├── test_transform.py
    └── test_validate.py
```
---

## Architecture overview

### Ingest layer

Responsible only for:
- reading input JSON
- handling file system errors
- returning either raw data or structured error information

No validation or business logic occurs here.

---

### Validation layer

Implemented using Pydantic models.

Responsibilities:
- strict schema enforcement
- type normalization
- rejection of unknown fields
- detailed validation error reporting

All validation failures are converted into a unified error structure.

---

### Transformation layer

Contains pure business logic.

Responsibilities:
- filtering active users
- mapping validated input models to output models

This layer performs no IO, logging, or printing.

---

### Output layer

Builds deterministic response structures.

Success example:
```json
{
  "statusCode": 200,
  "count": 5,
  "users": [...]
}
```
Error example:
```json
{
  "statusCode": 400,
  "error": {
    "code": "...",
    "message": "...",
    "details": [...]
  }
}
```
---

### Error model

All failures are represented using a single error contract:

- status_code
- code
- message
- details

This ensures predictable behavior across the entire pipeline.

---

### Logging and observability

Logging includes:
- request ID per execution
- step-by-step pipeline logs
- execution time measurement
- centralized log file output

This mirrors real backend observability patterns.

---

## Testing

XS14 includes comprehensive pytest coverage:

- validation logic
- transformation correctness
- output formatting
- full integration pipeline tests

Each layer is tested independently and as part of the complete flow.

---

## How to run locally (Python)

Create virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run tests:
```bash
pytest
```

Run pipeline:

PYTHONPATH is set so Python can resolve the src-based package structure.

```bash
export PYTHONPATH="$(pwd)/src" && echo $PYTHONPATH
```

Run with 'ok' data by default:
```bash
python -m xs14.main
```

Run with 'bad' data:
```bash
MODE=bad python -m xs14.main
```

## How to run with Docker

Build image:
```bash
docker build -t milosfaktor/xs14:v1 .
```

Run Pytest in docker:
```bash
docker run --rm milosfaktor/xs14:v1 pytest
```

Run with 'ok' data by default:
```bash
docker run --rm milosfaktor/xs14:v1
```

Run with 'bad' data:
```bash
docker run --rm -e MODE=bad milosfaktor/xs14:v1
```


---

## Learning outcomes

Through this exercise, I learned:

- how backend pipelines are structured
- how validation differs from transformation
- why strict schemas matter
- how predictable error contracts are designed
- how logging supports debugging
- how testing protects system behavior

This project represents foundational backend engineering
before introducing frameworks, APIs, or cloud services.

