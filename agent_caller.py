import os
from dotenv import load_dotenv
from ibm_watsonx_ai import APIClient, Credentials
# FIX: This line prevents the NameError
from agents_config import AGENTS_DEPLOYMENTS 

load_dotenv()

# Creds cleanup
API_KEY = os.getenv("WATSONX_API_KEY").strip().replace('"', '')
URL = os.getenv("WATSONX_URL").strip().replace('"', '')
SPACE_ID = os.getenv("SPACE_ID").strip().replace('"', '')

client = APIClient(credentials=Credentials(api_key=API_KEY, url=URL))
client.set.default_space(SPACE_ID)

def call_agent(agent_name: str, prompt_text: str) -> str:
    deployment_id = AGENTS_DEPLOYMENTS.get(agent_name)
    if not deployment_id:
        return f"Error: {agent_name} ID not found."

    # The API strictly allows ONLY 'messages' (and context/tools)
    # Removing 'parameters' fixes the 400 Json document validation error.
    messages = [
        {
            "role": "user",
            "content": prompt_text
        }
    ]

    try:
        # Pass ONLY messages. Let the deployment handle the defaults.
        response = client.deployments.chat(
            deployment_id=deployment_id,
            messages=messages
        )
        
        if "choices" in response and len(response["choices"]) > 0:
            return response["choices"][0]["message"]["content"]
        
        return "Error: Received empty response from chat endpoint."

    except Exception as e:
        # This will catch if the SDK version requires a version param or other header
        return f"CRITICAL ERROR [{agent_name}]: {str(e)}"