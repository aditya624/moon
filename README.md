# Moon MCP Server

Moon MCP Server is a template project for building Model Context Protocol (MCP) backends using [FastMCP](https://github.com/fastmcp). It is packaged with Poetry, ships with a lightweight Dockerfile, and exposes a simple `ping` tool to verify connectivity.

## Features

- ✅ FastMCP-powered MCP server with a FastAPI integration
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
poetry run uvicorn moon.main:app --host 0.0.0.0 --port 8000
```

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
