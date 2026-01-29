# errors.py

from dataclasses import dataclass


@dataclass
class ErrorInfo:
    status_code: int
    code: str
    message: str
    details: list[dict] | None
