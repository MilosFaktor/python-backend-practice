# ingest.py

from __future__ import annotations
from xs14.errors import ErrorInfo
import json


def read_json_file(json_path: str) -> dict | ErrorInfo:
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        return ErrorInfo(
            status_code=400,
            code="INGEST_ERROR",
            message="Input file not found",
            details=[{"path": json_path}],
        )

    except json.JSONDecodeError as e:
        return ErrorInfo(
            status_code=400,
            code="INGEST_ERROR",
            message="Invalid JSON",
            details=[{"path": json_path, "error": str(e)}],
        )

    except OSError as e:
        return ErrorInfo(
            status_code=400,
            code="INGEST_ERROR",
            message="Failed to read input file",
            details=[{"path": json_path, "error": str(e)}],
        )
