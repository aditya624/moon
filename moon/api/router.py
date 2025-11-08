"""FastAPI routes for health monitoring and diagnostics."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Health check", tags=["system"])
async def healthcheck() -> dict[str, str]:
    """Return a simple JSON response indicating the API is healthy."""

    return {"status": "ok"}


__all__ = ["router"]
