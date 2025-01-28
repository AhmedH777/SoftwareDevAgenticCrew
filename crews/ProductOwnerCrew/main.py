#!/usr/bin/env python
import sys
import warnings

from crew import ProductOwnerCrew
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
        ProductOwnerCrew(llm=llm).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train(inputs = None, n_iterations = 1, filename = "training.pkl"):
    """
    Train the crew for a given number of iterations.
    """
    try:
        ProductOwnerCrew(llm=llm).crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(task_id = None):
    """
    Replay the crew execution from a specific task.
    """
    try:
        ProductOwnerCrew(llm=llm).crew().replay(task_id=task_id)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(inputs = None, n_iterations = 1, openai_model_name = "gpt-4o"):
    """
    Test the crew execution and returns the results.
    """
    try:
        os.environ["OPENAI_API_KEY"] = api_key
        ProductOwnerCrew(llm=llm).crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    mode = input("Please select mode [run, train, replay, test]: ")

    inputs = {
    "programming_language": "Python",
    "software_blocks":"{      block_name: Task Class,      description: Represents a single task in the to-do list with attributes for description and status.,      input_list: [description],      output_list: [Task object with status set to Incomplete]    },    {      block_name: ToDoList Class,      description: Manages a collection of Task objects, providing methods to add, view, complete, and delete tasks.,      input_list: [description, task_id],      output_list: [List of tasks, Updated task status, Task deleted confirmation, Task saved to file, Tasks loaded from file]    },    {      block_name: FileHandler Class,      description: Handles file operations for saving and loading tasks to ensure data persistence.,      input_list: [tasks, filename],      output_list: [Tasks written to file, List of Task objects read from file]    },    {      block_name: CLI Class,      description: Manages the command-line interface for user interaction, capturing commands and executing them.,      input_list: [command],      output_list: [Menu displayed, User input captured, Command executed]    },    {      block_name: Main Application Logic,      description: Coordinates the overall application flow, initializing components and managing user interactions.,      input_list: [],      output_list: [Application started, Tasks loaded, Application exited with cleanup]    }" 
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