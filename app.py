import streamlit as st
from pipeline import process_input

st.set_page_config(page_title="Watsonx Multi-Agent Research System", layout="wide")
st.title("🎓 Multi-Agent Academic Assistant (Watsonx)")

# --- Sidebar Configuration ---
with st.sidebar:
    st.header("Settings")
    citation_style = st.selectbox("Citation style:", ["MLA", "IEEE", "None"])
    st.info("The Formatter agent will restructure the final output based on this style.")

# --- Main Input ---
user_input = st.text_area("Enter your research topic or query:", placeholder="e.g., Explain the legal implications of AI code...")

if st.button("Generate Report"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a query.")
    else:
        with st.spinner("🤖 Agents are collaborating..."):
            result = process_input(user_input, citation_style)
        
        st.divider()
        st.subheader("✅ Final Research Report")
        
        # FIX: Using st.markdown instead of st.text_area for formatting
        st.markdown(result)
        
        # --- Download Capability ---
        st.download_button(
            label="💾 Download Report as TXT",
            data=result,
            file_name="research_report.txt",
            mime="text/plain"
        )