"""Utility tools exposed by the MCP server."""
from fastmcp import FastMCP


def register_tools(server: FastMCP) -> None:
    """Register MCP tools with the provided :class:`FastMCP` server instance."""

    @server.tool(name="ping", description="Simple health-check tool")
    async def ping() -> str:  # noqa: WPS430 - nested function keeps registration local
        return "pong"


__all__ = ["register_tools"]
