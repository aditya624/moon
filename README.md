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

### Environment variables

The server reads its configuration from environment variables (optionally
loaded via a local `.env` file). The most common settings are listed below:

| Variable | Description | Default |
| --- | --- | --- |
| `MCP_TRANSPORT` | Transport type used by the MCP server. | `streamable-http` |
| `MCP_HOST` | Host interface the MCP server binds to. | `0.0.0.0` |
| `QDRANT_URL` | Base URL of the Qdrant instance supplying context. | `https://657e9ff8-daa0-4003-bf76-c531e697932d.europe-west3-0.gcp.cloud.qdrant.io:6333` |
| `QDRANT_API_KEY` | API key for the Qdrant instance. | _empty_ |
| `QDRANT_TOP_K` | Number of top search results to return. | `10` |
| `HF_TOKEN` | Hugging Face token used for embedding calls. | _empty_ |
| `HF_MODEL` | Hugging Face embedding model identifier. | `BAAI/bge-m3` |

### Running with Docker

```bash
docker build -t moon-mcp .
docker run --rm -p 8181:8181 --env-file .env moon-mcp
```

The Docker image runs `python moon/main.py`, matching the local execution flow. Update the `.env` file (or provide a different `--env-file`) to configure `MCP_HOST`, `MCP_PORT`, and other environment variables when running the container.

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
