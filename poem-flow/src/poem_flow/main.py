from poem_flow.crews.poem_crew.poem_crew import PoemCrew
from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv, find_dotenv
from random import randint 
from pydantic import BaseModel, Field
import os

_:bool = load_dotenv(find_dotenv())
model = os.getenv("MODEL")

class PoemConfig(BaseModel):
    sentence_count: int = 1
    poem: str = ""
    
# this is the main flow of the entire CrewAI project
class PoemFlow(Flow[PoemConfig]):
    @start()
    def gen_sentence_count(self):
        self.state.sentence_count = randint(1, 4)     
    
    @listen(gen_sentence_count)
    def generate_poem(self):
        result = PoemCrew().poem_crew().kickoff(
            inputs = {
                "sentence_count": self.state.sentence_count,
                "topic"         : "CrewAI"
                })
        self.state.poem = result.raw
    
    @listen(generate_poem)
    def save_poem(self):
        return {
            "poem": self.state.poem,
            "author": "Sufyan"
        }
    

def kickoff():
    flow = PoemFlow()
    response = flow.kickoff()
    print(f" Generated Topic:{response}")
    
    
def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()
