"""Application configuration settings."""
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Base application settings sourced from environment variables."""

    app_name: str = Field(default="Moon MCP Server", description="Service name")
    host: str = Field(default="0.0.0.0", description="Host interface for the MCP server")
    port: int = Field(default=8000, description="Port for the MCP server")

    model_config = {
        "env_prefix": "MOON_",
        "extra": "ignore",
    }


@lru_cache
def get_settings() -> Settings:
    """Return a cached instance of :class:`Settings`."""

    return Settings()


__all__ = ["Settings", "get_settings"]
