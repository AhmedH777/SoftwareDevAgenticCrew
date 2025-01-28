#!/usr/bin/env python
import sys
import warnings

from crew import IntegratorCrew
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
        IntegratorCrew(llm=llm).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train(inputs = None, n_iterations = 1, filename = "training.pkl"):
    """
    Train the crew for a given number of iterations.
    """
    try:
        IntegratorCrew(llm=llm).crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(task_id = None):
    """
    Replay the crew execution from a specific task.
    """
    try:
        IntegratorCrew(llm=llm).crew().replay(task_id=task_id)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(inputs = None, n_iterations = 1, openai_model_name = "gpt-4o"):
    """
    Test the crew execution and returns the results.
    """
    try:
        os.environ["OPENAI_API_KEY"] = api_key
        IntegratorCrew(llm=llm).crew().test(n_iterations=n_iterations, openai_model_name=openai_model_name, inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    mode = input("Please select mode [run, train, replay, test]: ")

    inputs = {
        "programming_language": "python",
        "client_requirements": "I want a To-Do List App. A user can create a to-do list where tasks can be added, viewed, completed, and deleted.Tasks should have:A description (e.g., Buy groceries).A status (e.g., Incomplete or Complete).Interaction should happen through a command-line interface.The program saves tasks to a file so they persist between sessions.",
        "software_architecture": "(programming_language: Python, software_blocks: (block_name: Task Model, description: Defines the structure and behavior of a task within the to-do list., dependencies: None, input_list: [Task description, Task status], output_list: [Updated task status, Updated task description])\n(block_name: To-Do List Manager, description: Manages the collection of tasks, providing functionality to add, view, delete, save, and load tasks., dependencies: Task Model, input_list: [Task object, File path for saving/loading], output_list: [List of tasks, Confirmation of task operations])\n(block_name: File Persistence, description: Handles saving and loading of tasks to and from a file to ensure data persistence., dependencies: To-Do List Manager, input_list: [List of tasks, File path], output_list: [Persisted task data, Loaded task data])\n(block_name: Command-Line Interface (CLI), description: Provides a command-line interface for user interaction, allowing users to manage their to-do list., dependencies: To-Do List Manager, input_list: [User commands], output_list: [User feedback, Task operation results])\n(block_name: Main Application Loop, description: Continuously prompts the user for input and processes commands until the user chooses to exit., dependencies: Command-Line Interface (CLI), input_list: [User input], output_list: [Application state, User prompts])\n(block_name: Error Handling, description: Manages errors related to user input and file operations to ensure smooth application execution., dependencies: All other blocks, input_list: [Potential errors], output_list: [Error messages, Error resolutions])\n)",
        "software_files":"software_files:str((programming_language: Python, software_file_name: task_model.py, purpose: Defines the structure and behavior of a task within the to-do list., software_component: Class, software_component_name: Task, dependencies: None, description: Defines the structure and behavior of a task within the to-do list., inputs: (description: str, status: str), outputs: (Updated task status: str, Updated task description: str), requirements: None, methods: (update_status: Updates the task status., update_description: Updates the task description.))(programming_language: Python, software_file_name: todo_list_manager.py, purpose: Manages the collection of tasks, providing functionality to add, view, delete, save, and load tasks., software_component: Class, software_component_name: ToDoListManager, dependencies: Task Model, description: Manages the collection of tasks, providing functionality to add, view, delete, save, and load tasks., inputs: (Task object: Task, File path for saving/loading: str), outputs: (List of tasks: List[Task], Confirmation of task operations: bool), requirements: Task Model, methods: (add_task: Adds a new task to the list., view_tasks: Returns the list of tasks., delete_task: Deletes a task by its ID and returns confirmation., save_tasks: Saves tasks to a file and returns confirmation., load_tasks: Loads tasks from a file and returns the list of tasks.))(programming_language: Python, software_file_name: file_persistence.py, purpose: Handles saving and loading of tasks to and from a file to ensure data persistence., software_component: Class, software_component_name: FilePersistence, dependencies: To-Do List Manager, description: Handles saving and loading of tasks to and from a file to ensure data persistence., inputs: (List of tasks: List[Task], File path: str), outputs: (Persisted task data: bool, Loaded task data: List[Task]), requirements: To-Do List Manager, methods: (save_to_file: Saves the list of tasks to a file., load_from_file: Loads tasks from a file and returns them.))(programming_language: Python, software_file_name: cli.py, purpose: Provides a command-line interface for user interaction, allowing users to manage their to-do list., software_component: Class, software_component_name: CommandLineInterface, dependencies: To-Do List Manager, description: Provides a command-line interface for user interaction, allowing users to manage their to-do list., inputs: (User commands: str), outputs: (User feedback: str, Task operation results: None), requirements: To-Do List Manager, methods: (process_command: Processes user commands and returns feedback., display_tasks: Displays the list of tasks to the user.))(programming_language: Python, software_file_name: main_application.py, purpose: Continuously prompts the user for input and processes commands until the user chooses to exit., software_component: Function, software_component_name: main_loop, dependencies: Command-Line Interface (CLI), description: Continuously prompts the user for input and processes commands until the user chooses to exit., inputs: (User input: str), outputs: (Application state: None, User prompts: str), requirements: Command-Line Interface (CLI), methods: ())(programming_language: Python, software_file_name: error_handling.py, purpose: Manages errors related to user input and file operations to ensure smooth application execution., software_component: Class, software_component_name: ErrorHandler, dependencies: All other blocks, description: Manages errors related to user input and file operations to ensure smooth application execution., inputs: (Potential errors: Exception), outputs: (Error messages: str, Error resolutions: str), requirements: All other blocks, methods: (handle_input_error: Manages errors related to user input and returns error messages., handle_file_error: Manages errors related to file operations and returns error messages.))),",
        "project_files_directory" : "D:\Projects\AI_Agents2\projectDir",
        "integrated_files_dump_directory" : "D:\Projects\AI_Agents2\integratedProj"
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