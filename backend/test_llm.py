"""Test script for LLM models."""

import asyncio
from .openrouter import query_models_parallel
from .config import COUNCIL_MODELS

async def test_all_models():
    """Test all configured LLM models with a simple prompt."""
    # Simple test prompt
    prompt = "你好，你是谁？请简要介绍一下自己。"
    messages = [{"role": "user", "content": prompt}]
    
    print("Testing all configured LLM models...")
    print(f"Test prompt: {prompt}")
    print("=" * 80)
    
    # Query all models in parallel
    responses = await query_models_parallel(COUNCIL_MODELS, messages)
    
    # Print results
    for model_name, response in responses.items():
        print(f"Model: {model_name}")
        if response:
            print(f"Response: {response['content'][:200]}..." if len(response['content']) > 200 else f"Response: {response['content']}")
        else:
            print("Error: No response received")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(test_all_models())