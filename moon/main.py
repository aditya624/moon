from typing import Annotated
from pydantic import Field
from fastmcp import FastMCP
from moon.tools.knowledge import Knowledge
from moon.config import settings

mcp_knowledge = FastMCP("Knowledge 🚀")
knowledge = Knowledge()

@mcp_knowledge.tool(
    name="get_knowledge",
    description="Search for knowledge",
)
def get_knowledge(
        query: Annotated[str, Field(description="The query to search for knowledge")]
    ) -> str:
    """Search for knowledge"""
    context = knowledge.search(query)
    return context

if __name__ == "__main__":
    mcp_knowledge.run(transport=settings.mcp.mcp_transport, host=settings.mcp.mcp_host, port=settings.mcp.mcp_port)