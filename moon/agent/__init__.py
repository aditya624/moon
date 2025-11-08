"""Agent orchestration utilities for the Moon MCP server."""

from typing import Any, Dict


def build_initial_state() -> Dict[str, Any]:
    """Return the initial agent state."""

    return {}


__all__ = ["build_initial_state"]
