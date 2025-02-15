from pydantic import BaseModel
from typing import List
from langchain_core.messages import AIMessage, HumanMessage
from agent import get_response_from_ai_agent
import uvicorn

# Step 1: Create schema for validation
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str 
    messages: List[str]
    allow_search: bool
    
#Step 2: Fast API end points
from fastapi import FastAPI

app = FastAPI(title="Personal AI Agent by Sufyan Ahmed")

@app.post("/generate-response/")
async def generate_response(request: RequestState):
    query = [HumanMessage(content=msg) for msg in request.messages]
    llm_id = request.model_name
    provider = request.model_provider
    system_prompt = request.system_prompt
    allow_search = request.allow_search
    
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="127.0.0.1", port=8123, reload=True)

