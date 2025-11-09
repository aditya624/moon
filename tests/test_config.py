import importlib
import sys

import pytest

ENV_VARS = {
    "APP_NAME": "moon",
    "VERSION": "0.1.0",
    "SERVICE_ENV": "local",
    "REQUEST_TIMEOUT_S": "350",
    "MCP_TRANSPORT": "streamable-http",
    "MCP_HOST": "0.0.0.0",
    "MCP_PORT": "8181",
    "HF_TOKEN": "",
    "HF_MODEL": "BAAI/bge-m3",
    "EMBEDDING_TIMEOUT_S": "300",
    "QDRANT_URL": "https://657e9ff8-daa0-4003-bf76-c531e697932d.europe-west3-0.gcp.cloud.qdrant.io:6333",
    "QDRANT_API_KEY": "",
    "QDRANT_COLLECTION": "internal_knowledge",
    "QDRANT_TOP_K": "10",
}


def reload_config_module():
    sys.modules.pop("moon.config", None)
    return importlib.import_module("moon.config")


def clear_env(monkeypatch):
    for name in ENV_VARS:
        monkeypatch.delenv(name, raising=False)


@pytest.mark.parametrize("variable", list(ENV_VARS))
def test_settings_default_values_match_expected(monkeypatch, variable):
    clear_env(monkeypatch)

    config_module = reload_config_module()
    settings = config_module.settings

    expected_value = ENV_VARS[variable]

    match variable:
        case "APP_NAME":
            assert settings.app_name == expected_value
        case "VERSION":
            assert settings.version == expected_value
        case "SERVICE_ENV":
            assert settings.env == expected_value
        case "REQUEST_TIMEOUT_S":
            assert settings.request_timeout_s == int(expected_value)
        case "MCP_TRANSPORT":
            assert settings.mcp.mcp_transport == expected_value
        case "MCP_HOST":
            assert settings.mcp.mcp_host == expected_value
        case "MCP_PORT":
            assert settings.mcp.mcp_port == int(expected_value)
        case "HF_TOKEN":
            assert settings.embedding.token == expected_value
        case "HF_MODEL":
            assert settings.embedding.model == expected_value
        case "EMBEDDING_TIMEOUT_S":
            assert settings.embedding.timeout_s == int(expected_value)
        case "QDRANT_URL":
            assert settings.qdrant.url == expected_value
        case "QDRANT_API_KEY":
            assert settings.qdrant.api_key == expected_value
        case "QDRANT_COLLECTION":
            assert settings.qdrant.collection == expected_value
        case "QDRANT_TOP_K":
            assert settings.qdrant.top_k == int(expected_value)


def test_settings_reads_environment_overrides(monkeypatch):
    overrides = {
        "APP_NAME": "custom-moon",
        "VERSION": "1.2.3",
        "SERVICE_ENV": "production",
        "REQUEST_TIMEOUT_S": "120",
        "MCP_TRANSPORT": "sse",
        "MCP_HOST": "127.0.0.1",
        "MCP_PORT": "9090",
        "HF_TOKEN": "secret-token",
        "HF_MODEL": "sentence-transformers/all-MiniLM-L6-v2",
        "EMBEDDING_TIMEOUT_S": "30",
        "QDRANT_URL": "http://localhost:6333",
        "QDRANT_API_KEY": "api-key",
        "QDRANT_COLLECTION": "test_collection",
        "QDRANT_TOP_K": "3",
    }

    clear_env(monkeypatch)
    for name, value in overrides.items():
        monkeypatch.setenv(name, value)

    config_module = reload_config_module()
    settings = config_module.settings

    assert settings.app_name == "custom-moon"
    assert settings.version == "1.2.3"
    assert settings.env == "production"
    assert settings.request_timeout_s == 120

    assert settings.mcp.mcp_transport == "sse"
    assert settings.mcp.mcp_host == "127.0.0.1"
    assert settings.mcp.mcp_port == 9090

    assert settings.embedding.token == "secret-token"
    assert settings.embedding.model == "sentence-transformers/all-MiniLM-L6-v2"
    assert settings.embedding.timeout_s == 30

    assert settings.qdrant.url == "http://localhost:6333"
    assert settings.qdrant.api_key == "api-key"
    assert settings.qdrant.collection == "test_collection"
    assert settings.qdrant.top_k == 3
