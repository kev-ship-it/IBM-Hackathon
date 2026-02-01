from agent_caller import call_agent
from agents_config import AGENTS_DEPLOYMENTS

def run_multi_domain(user_input: str) -> str:
    # This calls your new analyzer prompt
    selected_key = call_agent("input_analyzer", user_input).strip().lower()
    
    # Safety: Ensure the key actually exists in your config
    if selected_key not in AGENTS_DEPLOYMENTS:
        selected_key = "english" 

    # Execute the chain
    domain_response = call_agent(selected_key, user_input)
    return domain_response