from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class MCPConfig(BaseModel):
    mcp_transport: str = os.getenv("MCP_TRANSPORT", "streamable-http")
    mcp_host: str = os.getenv("MCP_HOST", "0.0.0.0")
    mcp_port: int = int(os.getenv("MCP_PORT", "8181"))

class EmbeddingConfig(BaseModel):
    token: str = os.getenv("HF_TOKEN", "")
    model: str = os.getenv("HF_MODEL", "BAAI/bge-m3")
    timeout_s: int = int(os.getenv("EMBEDDING_TIMEOUT_S", "300"))

class QdrantConfig(BaseModel):
    url: str = os.getenv("QDRANT_URL", "https://657e9ff8-daa0-4003-bf76-c531e697932d.europe-west3-0.gcp.cloud.qdrant.io:6333")
    api_key: str = os.getenv("QDRANT_API_KEY", "")
    collection: str = os.getenv("QDRANT_COLLECTION", "internal_knowledge")
    top_k: int = int(os.getenv("QDRANT_TOP_K", "10"))

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "moon")
    version: str = os.getenv("VERSION", "0.1.0")
    env: str = os.getenv("SERVICE_ENV", "local")
    request_timeout_s: int = int(os.getenv("REQUEST_TIMEOUT_S", "350"))

    mcp: MCPConfig = MCPConfig()
    qdrant: QdrantConfig = QdrantConfig()
    embedding: EmbeddingConfig = EmbeddingConfig()

settings = Settings()
