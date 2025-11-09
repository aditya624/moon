from typing import Annotated
from pydantic import Field
from fastmcp import FastMCP
from moon.tools.knowledge import Knowledge

mcp = FastMCP("Knowledge 🚀")
knowledge = Knowledge()

@mcp.tool(
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
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8181)