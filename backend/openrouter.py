"""API client for making LLM requests to various providers."""

from openai import OpenAI
from typing import List, Dict, Any, Optional


async def query_model(
    model_config: Dict[str, Any],
    messages: List[Dict[str, str]],
    timeout: float = 120.0
) -> Optional[Dict[str, Any]]:
    """
    Query a single model via its API.

    Args:
        model_config: Model configuration dict with 'name', 'api_key', 'api_url', and 'model'
        messages: List of message dicts with 'role' and 'content'
        timeout: Request timeout in seconds

    Returns:
        Response dict with 'content' and optional 'reasoning_details', or None if failed
    """
    model_name = model_config['name']
    api_key = model_config['api_key']
    api_url = model_config['api_url']
    model = model_config['model']

    try:
        # Initialize OpenAI client
        client = OpenAI(
            api_key=api_key,
            base_url=api_url,
        )

        # Call the model
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=2048,
            top_p=0.95,
        )

        # Get the response
        response = completion.choices[0].message.content

        return {
            'content': response,
            'reasoning_details': None
        }

    except Exception as e:
        print(f"Error querying model {model_name}: {e}")
        return None


async def query_models_parallel(
    model_configs: List[Dict[str, Any]],
    messages: List[Dict[str, str]]
) -> Dict[str, Optional[Dict[str, Any]]]:
    """
    Query multiple models in parallel.

    Args:
        model_configs: List of model configuration dicts
        messages: List of message dicts to send to each model

    Returns:
        Dict mapping model name to response dict (or None if failed)
    """
    import asyncio

    # Create tasks for all models
    tasks = [query_model(model_config, messages) for model_config in model_configs]

    # Wait for all to complete
    responses = await asyncio.gather(*tasks)

    # Map model names to their responses
    return {model_config['name']: response for model_config, response in zip(model_configs, responses)}
