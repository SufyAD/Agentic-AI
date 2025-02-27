from poem_flow.crews.poem_crew.poem_crew import PoemCrew
from crewai.flow.flow import Flow, listen, start
from litellm import completion
from dotenv import load_dotenv, find_dotenv
import os

_:bool = load_dotenv(find_dotenv())
model = os.getenv("MODEL")

# this is the main flow of the entire CrewAI project
class PeomFlow(Flow):
    @start()
    def generate_poem(self):
        result = PoemCrew().poem_crew().kickoff(
            inputs = {
                'topic': "generate a poem on the topic of LangGraph" 
            }
        )
        print(result.raw)
        return result

def kickoff():
    flow = PeomFlow()
    response = flow.kickoff()
    print(f" Generated Topic:{response}")