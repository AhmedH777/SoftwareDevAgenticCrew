from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .config.in_out_struct import Architecture
import os


####################################################################################################
##################################### Crew Definition ##############################################
####################################################################################################
@CrewBase
class ArchitectCrew():
	"""ArchitectCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, llm: LLM):
		self.llm = llm
	
	@agent
	def architect(self) -> Agent:
		return Agent(
			config=self.agents_config['architect'],
			llm=self.llm,
			verbose=True
		)
		
	@agent
	def chief_architect(self) -> Agent:
		return Agent(
			config=self.agents_config['chief_architect'],
			llm=self.llm,
			verbose=True
		)
	
	
	@task
	def architect_task(self) -> Task:
		return Task(
			config=self.tasks_config['architect_task'],
			verbose=True
		)


	@task
	def chief_architect_task(self) -> Task:
		return Task(
			config=self.tasks_config['chief_architect_task'],
			output_pydantic = Architecture,
			verbose=True		
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the ArchitectCrew crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			llm=self.llm,
			verbose=True
			)
