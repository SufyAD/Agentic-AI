from crewai import Agent, Task, Crew
from crewai.project import CrewBase, agent, task, crew

@CrewBase
class PoemCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def poem_generator(self):
        return Agent(
            config = self.agents_config["poem_generator"],
        )

    @task
    def generate_poem(self):
        return Task(
            config = self.tasks_config["generate_poem"],
        )
        
    @crew
    def poem_crew(self):
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            verbose = True,
        )

    