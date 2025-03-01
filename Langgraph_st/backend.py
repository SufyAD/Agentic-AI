from pydantic import BaseModel
from typing import List
from langchain_core.messages import AIMessage, HumanMessage
from agent import get_response_from_ai_agent
import uvicorn
from fastapi import FastAPI, HTTPException

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gemini-1.5-flash"]

# Step 1: Create schema for validation
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str 
    messages: List[str]
    allow_search: bool
    
#Step 2: Fast API end points
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Personal AI Agent by Sufyan Ahmed")

@app.post("/chat")
async def generate_response(request: RequestState):
    """
     API Endpoint to interact with the Chatbot using LangGraph and search tools.
     It dynamically selects the model specified in the request
    """
    
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise HTTPException(status_code=400, detail="Invalid AI model specified")
    
    query = [HumanMessage(content=msg) for msg in request.messages]
    llm_id = request.model_name
    provider = request.model_provider
    system_prompt = request.system_prompt
    allow_search = request.allow_search
    
    
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return {"response": response}
    
    
if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)

