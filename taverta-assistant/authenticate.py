# Import standard libraries
import os

# Import third-party libraries
from flask import request, jsonify

VALID_TOKEN = os.getenv("API_AUTH_TOKEN", "fallback-token")

# Function to validate request authorization token
def require_auth():
    """
    Checks for a valid Bearer token in the Authorization header.

    Returns:
        Response | None: Returns an error response if unauthorized, otherwise None.
    """
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != f"Bearer {VALID_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
    return None

# Print confirmation message
print("\n✅ authenticate.py successfully executed")
