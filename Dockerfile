# --- Base image ---
FROM python:3.11-slim

# --- Set working directory ---
WORKDIR /app

# --- Install system dependencies for building (if needed) ---
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

# --- Copy requirements and install deps ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy application code ---
COPY src/ src/
COPY tests/ tests/

# --- Make entrypoint executable ---
RUN chmod +x src/entrypoint.sh

# --- Non-root user for security ---
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# --- Set PYTHONPATH ---
ENV PYTHONPATH=/app/src

# --- Entrypoint ---
ENTRYPOINT ["sh", "/app/src/entrypoint.sh"]

# --- Default command ---
CMD ["stream"]
