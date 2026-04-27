# Build
FROM cgr.dev/chainguard/python:latest-dev as build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin":$PATH
WORKDIR /app
RUN python -m venv venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime
FROM cgr.dev/chainguard/python:latest
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"
COPY --from=build /app/venv /app/venv
COPY src/ .
EXPOSE 5000
ENTRYPOINT ["python", "/app/script.py"]