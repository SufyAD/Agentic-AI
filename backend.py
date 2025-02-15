from pydantic import BaseModel
from typing import List
from langchain_core.messages import AIMessage, MessagesState

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str 
    messages: List[str]
    allow_search: bool
    
#Step 2: Fast API end points
from fastapi import FastAPI

app = FastAPI(title="Personal AI Agent by Sufyan Ahmed")

    
    
    
