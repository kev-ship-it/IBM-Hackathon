# pipeline.py
from router import run_multi_domain

def process_input(user_input: str, citation_style="MLA") -> str:
    """
    Full pipeline: input -> multi-domain routing -> formatter.
    """
    output = run_multi_domain(user_input)

    # Optional citation style instruction
    if citation_style.upper() in ["MLA", "IEEE"]:
        output = run_multi_domain(f"Format in {citation_style} style:\n{output}")

    return output
