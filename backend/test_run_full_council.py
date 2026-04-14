"""Test script for run_full_council function."""

import asyncio
from .council import run_full_council

async def test_run_full_council():
    """Test the run_full_council function."""
    # Test query
    user_query = "你好，你是谁？请简要介绍一下自己。"
    
    print("Testing run_full_council...")
    print(f"Test query: {user_query}")
    print("=" * 80)
    
    # Call the function
    stage1_results, stage2_results, stage3_result, metadata = await run_full_council(user_query)
    
    # Print stage 1 results
    print("STAGE 1: Individual Responses")
    print("-" * 80)
    for result in stage1_results:
        print(f"Model: {result['model']}")
        print(f"Response: {result['response'][:200]}..." if len(result['response']) > 200 else f"Response: {result['response']}")
        print("-" * 80)
    
    # Print stage 2 results
    print("STAGE 2: Peer Rankings")
    print("-" * 80)
    for result in stage2_results:
        print(f"Model: {result['model']}")
        print(f"Ranking: {result['ranking'][:200]}..." if len(result['ranking']) > 200 else f"Ranking: {result['ranking']}")
        print(f"Parsed Ranking: {result['parsed_ranking']}")
        print("-" * 80)
    
    # Print stage 3 result
    print("STAGE 3: Final Synthesis")
    print("-" * 80)
    print(f"Model: {stage3_result['model']}")
    print(f"Response: {stage3_result['response'][:200]}..." if len(stage3_result['response']) > 200 else f"Response: {stage3_result['response']}")
    print("-" * 80)
    
    # Print metadata
    print("METADATA")
    print("-" * 80)
    print(f"Label to Model: {metadata.get('label_to_model', {})}")
    print(f"Aggregate Rankings: {metadata.get('aggregate_rankings', [])}")
    print("-" * 80)
    
    if not stage1_results:
        print("Error: No models responded successfully")
    else:
        print("Test completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_run_full_council())