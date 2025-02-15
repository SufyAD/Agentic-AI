import os
from dotenv import load_dotenv

load_dotenv()

# Fetch keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPEN_AI_KEY = os.getenv("DEEP_SEEK_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage

#define LLMs/Models - they are replaced later with user defined LLM Model
# gemini_llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)
# groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="Google-Gemini":
        llm=ChatGoogleGenerativeAI(model=llm_id, api_key=GEMINI_API_KEY)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    
    agent=create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]


#### Testing the Agent

# def test_ai_agent():
#     llm_id = "gemini-1.5-flash"  # Example model
#     query = [HumanMessage(content="What is the capital of Pakistan?")]
#     allow_search = False
#     system_prompt = "Answer concisely."
#     provider = "Google-Gemini"
    
#     response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
#     print("AI Response:", response)

# # Run the test
# test_ai_agent()