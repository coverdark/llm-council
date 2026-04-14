"""Configuration for the LLM Council."""

import os
from dotenv import dotenv_values

# Load configuration directly from .env file
config = dotenv_values()

# Alibaba Cloud API configuration (Qwen model)
LLM_API_KEY = "sk-6b0cc49523ed491d95ae998874619516"
LLM_API_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
LLM_API_MODEL = "qwen3.6-plus"

# Council members - list of model configurations
COUNCIL_MODELS = [
    {
        "name": "alibaba/qwen3.6-plus-1",
        "api_key": LLM_API_KEY,
        "api_url": LLM_API_BASE_URL,
        "model": LLM_API_MODEL
    },
    {
        "name": "alibaba/qwen3.6-plus-2",
        "api_key": LLM_API_KEY,
        "api_url": LLM_API_BASE_URL,
        "model": LLM_API_MODEL
    },
    {
        "name": "alibaba/qwen3.6-plus-3",
        "api_key": LLM_API_KEY,
        "api_url": LLM_API_BASE_URL,
        "model": LLM_API_MODEL
    },
    {
        "name": "alibaba/qwen3.6-plus-4",
        "api_key": LLM_API_KEY,
        "api_url": LLM_API_BASE_URL,
        "model": LLM_API_MODEL
    }
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "alibaba/qwen3.6-plus-1"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
