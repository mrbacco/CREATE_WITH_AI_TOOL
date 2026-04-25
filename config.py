"""
GEN_AI_TOOL project
Router and AI responses comparison tool done with flask

mrbacco04@gmail.com
Q2, 2026

Runtime configuration — all values are read from environment variables so that
no secrets are ever hardcoded.  A local .env file is loaded automatically when
python-dotenv is available (development convenience).
"""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# ---------------------------------------------------------------------------
# LLM / provider settings
# ---------------------------------------------------------------------------

OLLAMA_DEFAULT_MODEL: str = os.getenv("OLLAMA_DEFAULT_MODEL", "phi3")

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY", "")
OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY", "")

OLLAMA_CLOUD_BASE_URL: str = os.getenv("OLLAMA_CLOUD_BASE_URL", "https://ollama.com")

OPENROUTER_SITE_URL: str = os.getenv("OPENROUTER_SITE_URL", "http://localhost:5050")
OPENROUTER_APP_NAME: str = os.getenv("OPENROUTER_APP_NAME", "CREATE_WITH_AI")

LMSTUDIO_URL: str = os.getenv("LMSTUDIO_URL", "http://localhost:1234/v1")

# ---------------------------------------------------------------------------
# Storage paths
# ---------------------------------------------------------------------------

UPLOAD_FOLDER: str = os.getenv("UPLOAD_FOLDER", "uploads")
RAG_INDEX_FILE: str = os.getenv("RAG_INDEX_FILE", "data/rag_index.json")

# ---------------------------------------------------------------------------
# Tuning parameters
# ---------------------------------------------------------------------------

MAX_CONTEXT_MESSAGES: int = int(os.getenv("MAX_CONTEXT_MESSAGES", "20"))
COMPARE_MAX_WORKERS: int = int(os.getenv("COMPARE_MAX_WORKERS", "4"))

RAG_TOP_K: int = int(os.getenv("RAG_TOP_K", "4"))
RAG_CHUNK_SIZE: int = int(os.getenv("RAG_CHUNK_SIZE", "900"))
RAG_CHUNK_OVERLAP: int = int(os.getenv("RAG_CHUNK_OVERLAP", "120"))
RAG_VECTOR_DIMS: int = int(os.getenv("RAG_VECTOR_DIMS", "192"))
RAG_MAX_SNIPPET_CHARS: int = int(os.getenv("RAG_MAX_SNIPPET_CHARS", "800"))

# ---------------------------------------------------------------------------
# Feature flags
# ---------------------------------------------------------------------------

ENABLE_BAC_LOGS: bool = os.getenv("ENABLE_BAC_LOGS", "false").lower() in ("1", "true", "yes")
APP_DEBUG: bool = os.getenv("APP_DEBUG", "false").lower() in ("1", "true", "yes")
