# Import third-party libraries
from flask import Flask, request, jsonify

# Import project-specific modules
from authenticate import require_auth
from prompt import ask_openai
from envrionment import DEBUG, PORT  # Note: typo in 'envrionment'

app = Flask(__name__)

try:
    # Import optional RAG modules
    from retrieve import retrieve_context
    from augment import augment_prompt
    RAG_ENABLED = True
except ImportError:
    RAG_ENABLED = False

# Function to handle chat requests via POST and return GPT-generated responses
@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle chat interactions.

    Verifies authentication, optionally applies RAG logic,
    sends the final prompt to OpenAI, and returns the reply.

    Returns:
        Response: JSON object containing the reply or error message.
    """
    auth_error = require_auth()
    if auth_error:
        return auth_error

    data = request.json
    prompt = data.get("message", "")
    if not prompt:
        return jsonify({"error": "No message provided"}), 400

    if RAG_ENABLED:
        context = retrieve_context(prompt)
        prompt = augment_prompt(prompt, context)

    reply = ask_openai(prompt)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=DEBUG, port=PORT)

# Print confirmation message
print("\n✅ main.py successfully executed")
