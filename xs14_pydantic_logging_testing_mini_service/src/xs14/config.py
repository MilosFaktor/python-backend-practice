# src/xs14/config.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]  # repo root if src/xs14/config.py


@dataclass(frozen=True)
class Settings:
    log_level: str = "INFO"
    logs_dir: Path = PROJECT_ROOT / "logs"
    log_file: Path = logs_dir / "xs14.log"

    data_ok: Path = PROJECT_ROOT / "data" / "sample_ok.json"
    data_bad: Path = PROJECT_ROOT / "data" / "sample_bad.json"

    # choose which file main reads ("ok" or "bad")
    mode: str = "ok"


settings = Settings()
