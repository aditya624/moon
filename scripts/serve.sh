#!/usr/bin/env sh
set -euo pipefail

poetry run uvicorn moon.main:app --host "${HOST:-0.0.0.0}" --port "${PORT:-8000}"
