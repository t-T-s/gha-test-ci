# ── Build stage ──────────────────────────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# ── Runtime stage ─────────────────────────────────────────
FROM python:3.12-slim

WORKDIR /app
COPY --from=builder /install /usr/local
COPY src/ ./src/

ENV FLASK_ENV=production
ENV PORT=3000

EXPOSE 3000
CMD ["python", "-m", "src.server"]