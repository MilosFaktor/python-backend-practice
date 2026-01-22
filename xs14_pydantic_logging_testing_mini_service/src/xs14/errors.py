from dataclasses import dataclass


@dataclass
class ErrorInfo:
    status_code: int
    code: str
    message: str
    details: dict | None
