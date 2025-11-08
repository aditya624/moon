"""Application entrypoint for the Moon MCP server."""
from fastmcp import FastMCP
from fastapi import FastAPI

from .api.router import router as api_router
from .config import get_settings
from .tools import register_tools


def create_app() -> FastAPI:
    """Create and configure the FastMCP application."""

    settings = get_settings()
    server = FastMCP(name=settings.app_name)
    register_tools(server)

    app = server.app
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()


__all__ = ["app", "create_app"]
