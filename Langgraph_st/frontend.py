import streamlit as st
import requests


st.set_page_config(
    page_title="AI Agent",
    layout="centered"
)
st.title("AI Agent by M.Sufyan Ahmed")
st.write("This is a simple AI agent that uses a search engine to find information on a given topic.") #small description for the chatbot
system_prompt = st.text_area("Define your AI Agent's behavior here", placeholder="Example: You are a helpful assistant that can answer questions and help with tasks.", height=70)

GROQ_MODELS=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile"]
GOOGLE_MODELS=["gemini-1.5-flash"]

llm_provider=st.radio("Select the LLM provider", ["Groq", "Google"])

if llm_provider=="Groq":
    sel_model = st.selectbox("Select the model", GROQ_MODELS)
else:   
    sel_model = st.selectbox("Select the model", GOOGLE_MODELS)

user_query = st.text_input(
    "Ask anything:",
    key="user_input",
    placeholder="What is the capital of France?",
    on_change=None,
    args=None,
    kwargs=None
)

allow_web_search = st.checkbox("Allow websearch", value=False)

st.button("Ask Agent", type="primary", key="ask_button", use_container_width=False)

API_URL="http://127.0.0.1:8000/chat"

    
if user_query.strip():
    payload = {
        "model_name": sel_model,
        "model_provider": llm_provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        
        if "error" in response_data:
            st.write("OOPS! Error: ", response_data["error"])
        else:
            st.subheader("Agent Response")
            final_response = response_data.get("response", "No response found")  # Extract the relevant field
            st.markdown(f"**Final Response**: {final_response}")
    else:
        st.write("OOPS! Error: ", response.status_code)


 



