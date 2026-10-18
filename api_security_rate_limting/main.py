from fastapi import FastAPI, Header, HTTPException
from collections import defaultdict
from time import time

app = FastAPI(
    title="API Security and Rate Limiting",
    version="1.0.0"
)

# Demo API key
API_KEY = "internship-demo-key"

# Rate limiting configuration
request_counts = defaultdict(list)
RATE_LIMIT = 5
WINDOW_SECONDS = 60


@app.get("/")
def home():
    return {
        "message": "API Security and Rate Limiting API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/secure")
def secure_api(
    x_api_key: str = Header(default=None),
    client_id: str = Header(default="anonymous")
):
    # Validate API key
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    # Check recent requests
    current_time = time()

    request_counts[client_id] = [
        t for t in request_counts[client_id]
        if current_time - t < WINDOW_SECONDS
    ]

    # Enforce rate limit
    if len(request_counts[client_id]) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later."
        )

    request_counts[client_id].append(current_time)

    return {
        "message": "Access granted",
        "client_id": client_id,
        "requests_remaining": (
            RATE_LIMIT - len(request_counts[client_id])
        )
    }from fastapi import FastAPI, Header, HTTPException
from collections import defaultdict
from time import time

app = FastAPI(
    title="API Security and Rate Limiting",
    version="1.0.0"
)

API_KEY = "internship-demo-key"

request_counts = defaultdict(list)
RATE_LIMIT = 5
WINDOW_SECONDS = 60


@app.get("/")
def home():
    return {
        "message": "API Security and Rate Limiting API is running"
    }


@app.get("/secure")
def secure_api(
    x_api_key: str = Header(default=None),
    client_id: str = Header(default="anonymous")
):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    now = time()

    recent_requests = [
        t for t in request_counts[client_id]
        if now - t < WINDOW_SECONDS
    ]

    if len(recent_requests) >= RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded. Try again later."
        )

    recent_requests.append(now)
    request_counts[client_id] = recent_requests

    return {
        "message": "Access granted",
        "client_id": client_id,
        "requests_remaining": RATE_LIMIT - len(recent_requests)
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
