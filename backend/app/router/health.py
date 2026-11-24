"""Health route for the FastAPI application."""

from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["health"])

@router.get("/health")
def health() -> dict[str, str]:
    """Endpoint returning a health check message."""
    return {"message": "Healthy"}
