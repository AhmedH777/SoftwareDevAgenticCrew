from crewai import Flow, LLM
from crewai.flow.flow import listen, start
from crews.CustomerServiceCrew.crew import CustomerServiceCrew
from crews.ArchitectCrew.crew import ArchitectCrew
from crews.ProductOwnerCrew.crew import ProductOwnerCrew
from crews.SoftwareDeveloperCrew.crew import SoftwareDeveloperCrew
from crews.IntegratorCrew.crew import IntegratorCrew
import os 
import json

####################################################################################################
##################################### Load Model Parameters ########################################
####################################################################################################
# importing necessary functions from dotenv library
from dotenv import load_dotenv 
# loading variables from .env file
load_dotenv() 

# accessing and printing value
model = os.getenv('MODEL')
api_key = os.getenv('API_KEY')


# Define Key as Environment Variable
os.environ["OPENAI_API_KEY"] = api_key

# Load LLM Model
llm = LLM(model=model, api_key=api_key, temperature=0)

####################################################################################################
##################################### Flow Definition ##############################################
####################################################################################################
class SoftwareDevPipeline(Flow):
    @start()
    def fetch_input(self):
        # Default inputs
        programming_language = "Python"
        requirements = "I want a function that calculate sum of two numbers"
        ############################################## Request User Input ################################################
        programming_language = input("What is your required programming language? ")
        requirements = input("What are your requirements? ")
        # Define Inputs
        inputs = {
                "programming_language": programming_language,
                "requirements" : requirements,
                }
        
        # Clarify Modes to the user
        print("#########################################################")
        print("Thanks for providing the requirements. You can now choose between two modes")
        print("Interactive Mode : A customer service specialist will interact with the user to enhance the requirements and gather more information")
        print("Direct Mode : Directly pass the requirements and start the project building process")
        print("#########################################################")

        # Request User Input for flow mode
        flow_mode = input("Which mode you want to run? (interactive , direct) : ")

        # Interactive Mode : A customer service specialist will interact with the user to gather requirements
        if flow_mode == "interactive":
            customer_service = CustomerServiceCrew(llm = llm).crew().kickoff(inputs=inputs)

            print("Customer Service Specialist has gathered the requirements")
            print("Programming Language : ", customer_service['programming_language'])
            print("Requirements : ", customer_service['requirements'])

            inputs = {
                "programming_language": customer_service['programming_language'],
                "requirements": customer_service['requirements']
            }
        # Direct Mode : Directly pass the requirements
        elif flow_mode == "direct":
            "Starting the project building process"
        else:
            print("Invalid mode selected. Exiting the process")
            return
        

        self.programming_language = inputs["programming_language"]
        self.user_requirements = inputs["requirements"]
        return inputs

    @listen(fetch_input)
    def define_architecture(self, inputs):
        architecture = ArchitectCrew(llm = llm).crew().kickoff(inputs=inputs)
        architecture = architecture.to_dict()
        return architecture['architecture_blocks']

    @listen(define_architecture)
    def define_coding_files_design(self, arch_blocks):
        software_blocks = ""
        for block in arch_blocks:
            software_blocks += str(block) + "\n"

        inputs = {
            "programming_language": self.programming_language,
            "software_blocks": software_blocks}
        self.arch_blocks = str(inputs)

        software_files_design = ProductOwnerCrew(llm = llm).crew().kickoff(inputs=inputs)
        return software_files_design
    
    @listen(define_coding_files_design)
    def software_files_implementation(self, software_files_design):
        software_files_code_list = []
        software_files_dict = software_files_design.pydantic.dict()
        self.product_owner_requirements = ""
        for file in software_files_dict['software_files_list']:
            filename = file['file_name']
            file_purpose = file['file_purpose']
            component = file['software_component']

            inputs = {
                "programming_language": self.programming_language,
                "software_file_name": filename,
                "purpose": file_purpose,
                "software_component": component['software_component_type'],
                "software_component_name": component['software_component_name'],
                "dependencies": component['dependencies'],
                "description": component['description'],
                "inputs": str(component['inputs']),
                "outputs": str(component['outputs']),
                "requirements": component['requirements'],
                "methods": str(component['methods']), 
                "break_down_of_project" : component['break_down_of_project'],
                "project_integration_considerations" : component['project_integration_considerations'],
                "user_requirements": self.user_requirements
                }
            self.product_owner_requirements += str(inputs) + "\n"

            software_files_code_list.append(SoftwareDeveloperCrew(llm = llm).crew().kickoff(inputs=inputs))
        return software_files_code_list
    
    @listen(software_files_implementation)
    def save_code(self, software_files_code_list):
        for file in software_files_code_list:
            file_dict = file.pydantic.dict()
            file_name = file_dict["software_file_name"]
            code = file_dict["software_file_implmentation"]
            filename_path = os.path.join("projectDir", file_name)
            with open(filename_path, "w") as file:
                file.write(code)

    @listen(save_code)
    def integrate_code(self):
        inputs = {
            "programming_language": self.programming_language,
            "client_requirements": self.user_requirements,
            "software_architecture": self.arch_blocks,
            "software_files": self.product_owner_requirements,
            "project_files_directory" : "projectDir",
            "integrated_files_dump_directory" : "D:\Projects\AI_Agents2\integratedProj"
        }

        integrated_files = IntegratorCrew(llm = llm).crew().kickoff(inputs=inputs)
        return integrated_files

    @listen(integrate_code)
    def save_integrated_code(self, integrated_files):
        integrated_files_dict = integrated_files.pydantic.dict()
        for file in integrated_files_dict['integrated_files_list']:
            file_name = file['file_name']
            code = file['code']
            filename_path = os.path.join("integratedProj", file_name)
            with open(filename_path, "w") as file:
                file.write(code)

if __name__ == "__main__":

    # Warning control
    import warnings
    warnings.filterwarnings('ignore')

    flow = SoftwareDevPipeline()
    flow.plot()
    arch = flow.kickoff()