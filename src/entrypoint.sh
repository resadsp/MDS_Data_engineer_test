#!/bin/sh
set -eu

case "$1" in
  stream)
    echo "[ENTRYPOINT] Running Stream Demo"
    python -m orchestration.run_stream_demo
    ;;
  files)
    echo "[ENTRYPOINT] Running Files Demo"
    python -m orchestration.run_files_demo
    ;;
  bonus)
    echo "[ENTRYPOINT] Running Tournament Demo"
    python -m bonus.run_tournament_demo
    ;;
  test)
    echo "[ENTRYPOINT] Running Tests"
    pytest tests/ --maxfail=1 -v
    ;;
  coverage)
    echo "[ENTRYPOINT] Running Coverage Report"
    pytest --cov=src --cov-config=.coveragerc --cov-report=term-missing --cov-report html:/app/htmlcov
    ;;
  *)
    echo "[ENTRYPOINT] Unknown or no argument, running Stream Demo by default"
    python -m orchestration.run_stream_demo
    ;;
esac
