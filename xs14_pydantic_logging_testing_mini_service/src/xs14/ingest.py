from __future__ import annotations
from errors import ErrorInfo
import json


def read_json_file(json_path: str) -> dict | ErrorInfo:
    try:
        with open(json_path, "r") as f:
            return json.load(f)

    except FileNotFoundError:
        return ErrorInfo(
            status_code=400,
            code="INGEST_ERROR",
            message="Input file not found",
            details={"path": json_path},
        )

    except json.decoder.JSONDecodeError as e:
        return ErrorInfo(
            status_code=400,
            code="INGEST_ERROR",
            message="Invalid JSON",
            details={"path": json_path, "error": str(e)},
        )

    except OSError as e:
        return ErrorInfo(
            status_code=400,
            code="INGEST_ERROR",
            message="Failed to read input file",
            details={"path": json_path, "error": str(e)},
        )
