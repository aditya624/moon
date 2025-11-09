# Moon MCP Server

Moon MCP Server is a template project for building Model Context Protocol (MCP) backends using [FastMCP](https://github.com/fastmcp). It is packaged with Poetry, ships with a lightweight Dockerfile, and exposes a simple `ping` tool to verify connectivity. The MCP server retrieves context from a Qdrant vector database, making it easy to supply relevant information to your agents.

## Features

- ✅ FastMCP-powered MCP server ready to run standalone
- ✅ Retrieves contextual knowledge from a Qdrant vector database
- ✅ Poetry project configuration targeting Python 3.11
- ✅ Dockerfile ready for container deployments
- ✅ Basic CI workflow (linting placeholder) for GitHub Actions

## Getting Started

### Prerequisites

- Python 3.11
- [Poetry](https://python-poetry.org/docs/#installation)

### Installation

```bash
poetry install
```

### Running the server

```bash
poetry run python moon/main.py
```

### Running with Docker

```bash
docker build -t moon-mcp .
docker run --rm -p 8181:8181 moon-mcp
```

The Docker image runs `python moon/main.py`, matching the local execution flow. Configure `MCP_HOST`, `MCP_PORT`, and other environment variables as needed when running the container.

### Running tests

```bash
poetry run pytest
```

## Project layout

```
moon/
├── .github/             GitHub Actions workflows
├── dockerfile           Production-ready container image definition
├── docs/                Documentation assets
├── moon/                Application source code
│   ├── agent/           LangGraph agent scaffolding
│   ├── api/             FastAPI routers and dependencies
│   ├── config.py        Pydantic settings module
│   ├── main.py          FastMCP application entrypoint
│   └── tools/           MCP tool definitions
├── pyproject.toml       Poetry configuration and dependencies
├── scripts/             Helper scripts for local development
├── tests/               Pytest-based unit and integration tests
└── README.md            Project overview and usage instructions
```

## License

This project is provided as-is. Feel free to adapt it for your own MCP services.
