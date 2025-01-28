from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from .config.in_out_struct import SoftwareFilesList
import os


####################################################################################################
##################################### Crew Definition ##############################################
####################################################################################################
@CrewBase
class ProductOwnerCrew():
	"""ProductOwnerCrew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, llm: LLM):
		self.llm = llm

	@agent
	def product_owner(self) -> Agent:
		return Agent(
			config=self.agents_config['product_owner'],
			llm=self.llm,
			verbose=True
		)
	
	@agent
	def chief_product_owner(self) -> Agent:
		return Agent(
			config=self.agents_config['chief_product_owner'],
			llm=self.llm,
			verbose=True
		)
	
	@task
	def product_owner_task(self) -> Task:
		return Task(
			config=self.tasks_config['product_owner_task'],
			verbose=True
		)

	@task
	def chief_product_owner_task(self) -> Task:
		return Task(
			config=self.tasks_config['chief_product_owner_task'],
			output_pydantic = SoftwareFilesList,
			verbose=True
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
