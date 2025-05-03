# Import standard libraries
import os

# Function to configure environment settings for local or VPS deployment
def load_environment_config():
    """
    Loads environment configuration variables.

    Returns:
        tuple: A tuple containing DEPLOY_MODE (str), PORT (int), and DEBUG (bool)
    """
    deploy_mode = os.getenv("DEPLOY_MODE", "local")
    port = int(os.getenv("PORT", 5000))
    debug = deploy_mode == "local"
    return deploy_mode, port, debug

# Assign global variables using the config function
DEPLOY_MODE, PORT, DEBUG = load_environment_config()

# Print confirmation message
print(f"\n✅ environment.py successfully executed")
