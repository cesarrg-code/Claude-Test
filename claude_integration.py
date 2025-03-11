"""
Basic Claude API Integration Example

This script demonstrates how to make a simple request to Claude's API.
To use this script, you'll need:
1. An Anthropic API key
2. The anthropic Python package installed (pip install anthropic)
"""

import os
import anthropic
from typing import Optional

def get_claude_response(
    prompt: str,
    model: str = "claude-3-7-sonnet-20250219",
    max_tokens: int = 1000,
    temperature: float = 0.7,
    api_key: Optional[str] = None
) -> str:
    """
    Send a prompt to Claude and get a response.
    
    Args:
        prompt: The text prompt to send to Claude
        model: Claude model version to use
        max_tokens: Maximum number of tokens to generate
        temperature: Controls randomness (0-1)
        api_key: Anthropic API key (if None, looks for ANTHROPIC_API_KEY env var)
    
    Returns:
        Claude's response as a string
    """
    # Use provided API key or get from environment
    if api_key is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if api_key is None:
            raise ValueError("No API key provided. Set ANTHROPIC_API_KEY environment variable or pass api_key parameter.")
    
    # Initialize the Anthropic client
    client = anthropic.Anthropic(api_key=api_key)
    
    # Make the API request
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # Return Claude's response text
    return message.content[0].text

if __name__ == "__main__":
    # Example usage
    user_prompt = "Explain three ways AI can be used to improve healthcare in rural areas."
    
    print("Sending prompt to Claude: ", user_prompt)
    print("\nClaude's response:")
    
    response = get_claude_response(user_prompt)
    print(response)
    
    # You can also use the function with custom parameters
    """
    response = get_claude_response(
        prompt="Write a short poem about technology and nature.",
        model="claude-3-opus-20240229",
        max_tokens=500,
        temperature=0.9,
        api_key="YOUR_API_KEY_HERE"  # Or omit to use environment variable
    )
    """
