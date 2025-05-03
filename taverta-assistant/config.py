# Import standard libraries
import os

# Function to load OpenAI API configuration
def load_openai_config():
    """
    Loads the OpenAI API key and model name from environment variables.

    Returns:
        tuple: A tuple containing the API key (str) and model name (str)
    """
    api_key = os.getenv("OPENAI_API_KEY", "your-api-key")
    model_name = "gpt-4o"
    return api_key, model_name

# Assign global variables using the config function
OPENAI_API_KEY, MODEL_NAME = load_openai_config()

# Print confirmation message
print("\n✅ config.py successfully executed")