# Import third-party libraries
import openai

# Import project-specific modules
from config import OPENAI_API_KEY, MODEL_NAME

openai.api_key = OPENAI_API_KEY

# Function to send a prompt to OpenAI and return the model's reply
def ask_openai(prompt: str) -> str:
    """
    Sends a user prompt to OpenAI's chat model and retrieves the response.

    Args:
        prompt (str): The user's input message.

    Returns:
        str: The model-generated reply text.
    """
    response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"].strip()

# Print confirmation message
print("\n✅ prompt.py successfully executed")
