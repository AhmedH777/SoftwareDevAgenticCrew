from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .config.in_out_struct import SoftwareFile
import os


####################################################################################################
##################################### Crew Definition ##############################################
####################################################################################################
@CrewBase
class SoftwareDeveloperCrew():
	"""Softdevcrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, llm):
		self.llm = llm
	
	@agent
	def developer(self) -> Agent:
		return Agent(
			config=self.agents_config['developer'],
			llm=self.llm,
			verbose=True
		)

	@agent
	def tester(self) -> Agent:
		return Agent(
			config=self.agents_config['tester'],
			llm=self.llm,
			allow_delegation=True,
			#allow_code_execution=True,
			#max_iter = 1,
			verbose=True
		)

	@agent
	def principal_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['principal_manager'],
			llm=self.llm,
			allow_delegation=True,
			verbose=True
		)
	
	@task
	def developer_task(self) -> Task:
		return Task(
			config=self.tasks_config['developer_task'],
			verbose=True,
			output_pydantic=SoftwareFile
		)

	@task
	def tester_task(self) -> Task:
		return Task(
			config=self.tasks_config['tester_task'],
			verbose=True
			)
	
	@task
	def principal_manager_task(self) -> Task:
		return Task(
			config=self.tasks_config['principal_manager_task'],
			verbose=True,
			context = [self.developer_task(), self.tester_task()],
			output_pydantic=SoftwareFile
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Softdevcrew crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			llm=self.llm,
			verbose=True
			)
