#!/usr/bin/env python
import sys
import warnings

from crew import SoftwareDeveloperCrew
from crewai import LLM
import os

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

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

llm = LLM(model=model, api_key=api_key, temperature=0)

####################################################################################################
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(inputs=None):
    """
    Run the crew.
    """  
    try:
        SoftwareDeveloperCrew(llm=llm).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train(inputs = None, n_iterations = 1, filename = "training.pkl"):
    """
    Train the crew for a given number of iterations.
    """
    try:
        SoftwareDeveloperCrew(llm=llm).crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(task_id = None):
    """
    Replay the crew execution from a specific task.
    """
    try:
        SoftwareDeveloperCrew(llm=llm).crew().replay(task_id=task_id)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(inputs = None, n_iterations = 1, openai_model_name = "gpt-4o"):
    """
    Test the crew execution and returns the results.
    """
    try:
        os.environ["OPENAI_API_KEY"] = api_key
        SoftwareDeveloperCrew(llm=llm).crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    mode = input("Please select mode [run, train, replay, test]: ")

    inputs = {
    "programming_language": "Python",
    "software_file_name": "todolist.py",
    "purpose":"Manages a collection of Task objects.",
    "software_component": "Class",
    "software_component_name": "ToDoList",
    "dependencies": "Task",
    "description": "Manages a collection of Task objects, providing methods to add, view, complete, and delete tasks.",
    "inputs": "{ description: str,task_id: int }",
    "outputs": "{          List of tasks: List[Task],          Updated task status: str,          Task deleted confirmation: str,          Task saved to file: str,          Tasks loaded from file: List[Task]        }",
    "requirements": "Methods to add, view, complete, delete tasks, save tasks to a file, and load tasks from a file.",
    "methods":"{          add_task: Method to add a new task.,          view_tasks: Method to view all tasks.,          complete_task: Method to mark a task as complete.,          delete_task: Method to delete a task.,          save_tasks: Method to save tasks to a file.,          load_tasks: Method to load tasks from a file.        }"
    }
    
    if mode == "run":
        run(inputs)
    elif mode == "train":
        train(inputs, n_iterations=1, filename="training.pkl")
    elif mode == "replay":
        replay(inputs)
    elif mode == "test":
        test(inputs, n_iterations=1, openai_model_name="gpt-4o")
    else:
        raise Exception("Invalid mode. Please select from [run, train, replay, test].")