# Function to combine retrieved context with user input for prompt augmentation
def augment_prompt(user_input: str, context: str) -> str:
    """
    Augments the user prompt with retrieved context for improved model response.

    Args:
        user_input (str): The original user input.
        context (str): Relevant information retrieved from data sources.

    Returns:
        str: A formatted prompt combining context and user message.
    """
    return f"Context: {context}\n\nUser: {user_input}"

# Print confirmation message
print("\n✅ augments.py successfully executed")
