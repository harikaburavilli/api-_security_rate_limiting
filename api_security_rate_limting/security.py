import os
import secrets
from fastapi import Header, HTTPException

API_KEY = os.getenv("API_KEY", "internship-demo-key")


def verify_api_key(
    x_api_key: str = Header(default=None)
):
    if not x_api_key or not secrets.compare_digest(
        x_api_key, API_KEY
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    return True
