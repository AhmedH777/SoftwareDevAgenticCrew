from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool
from .config.in_out_struct import IntegratedFilesList
from crewai_tools import DirectoryReadTool, FileReadTool


####################################################################################################
##################################### Crew Definition ##############################################
####################################################################################################
@CrewBase
class IntegratorCrew():
	"""IntegratorCrew crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	def __init__(self, llm):
		self.llm = llm
	


	@agent
	def integrator(self) -> Agent:
		return Agent(
			config=self.agents_config['integrator'],
			tools = [DirectoryReadTool(), FileReadTool()],
			llm=self.llm,
			verbose=True
		)


	@task
	def integrator_task(self) -> Task:
		return Task(
			config=self.tasks_config['integrator_task'],
			output_pydantic = IntegratedFilesList,
			verbose=True,
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the IntegratorCrew crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			llm=self.llm,
			verbose=True
			)
