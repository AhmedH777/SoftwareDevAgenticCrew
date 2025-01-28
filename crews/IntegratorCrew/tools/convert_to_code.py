import os
import json

def create_python_files(integrated_files_list):
    """
    Creates Python files from a list of file data dictionaries.
    
    :param integrated_files_list: List of dictionaries containing file names and their corresponding code.
    """
    try:
        # Ensure the target directory exists
        os.makedirs("generated_files", exist_ok=True)

        for file_data in integrated_files_list:
            file_name = file_data.get("file_name")
            code = file_data.get("code", "")

            if not file_name:
                print("File name is missing in one of the entries.")
                continue

            file_path = os.path.join("generated_files", file_name)
            
            # Write the code to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(code)

            print(f"File '{file_name}' created successfully at '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while creating files: {e}")

if __name__ == "__main__":

    data = {      "integrated_files_list": [
    {
      "file_name": "task_model.py",
      "code": "class Task:\n    def __init__(self, description, status='incomplete'):\n        if not isinstance(description, str) or not description.strip():\n            raise ValueError(\"Description must be a non-empty string.\")\n        if status not in ['incomplete', 'complete']:\n            raise ValueError(\"Status must be either 'incomplete' or 'complete'.\")\n        \n        self.description = description\n        self.status = status\n\n    def update_status(self, new_status):\n        if new_status not in ['incomplete', 'complete']:\n            raise ValueError(\"Status must be either 'incomplete' or 'complete'.\")\n        \n        self.status = new_status\n\n    def update_description(self, new_description):\n        if not isinstance(new_description, str) or not new_description.strip():\n            raise ValueError(\"Description must be a non-empty string.\")\n        \n        self.description = new_description"
    },
    {
      "file_name": "todo_list_manager.py",
      "code": "from typing import List\nfrom task_model import Task\n\nclass ToDoListManager:\n    def __init__(self):\n        self.tasks = []\n\n    def add_task(self, task: Task) -> bool:\n        self.tasks.append(task)\n        return True\n\n    def view_tasks(self) -> List[Task]:\n        return self.tasks\n\n    def delete_task(self, task_id: int) -> bool:\n        for task in self.tasks:\n            if task.task_id == task_id:\n                self.tasks.remove(task)\n                return True\n        return False\n\n    def save_tasks(self, file_path: str) -> bool:\n        try:\n            with open(file_path, 'w') as file:\n                for task in self.tasks:\n                    file.write(f'{task.task_id},{task.description}\\n')\n            return True\n        except IOError:\n            return False\n\n    def load_tasks(self, file_path: str) -> List[Task]:\n        loaded_tasks = []\n        try:\n            with open(file_path, 'r') as file:\n                for line in file:\n                    task_id, description = line.strip().split(',')\n                    loaded_tasks.append(Task(int(task_id), description))\n            self.tasks = loaded_tasks\n            return self.tasks\n        except IOError:\n            return []"       
    },
    {
      "file_name": "file_persistence.py",
      "code": "from typing import List\nfrom task_model import Task\n\nclass FilePersistence:\n    def save_to_file(self, tasks: List[Task], file_path: str) -> bool:\n        try:\n            with open(file_path, 'w') as file:\n                for task in tasks:\n                    file.write(f'{task.title},{task.description}\\n')\n            return True\n        except IOError as e:\n            print(f'An error occurred while saving tasks to file: {e}')\n            return False\n\n    def load_from_file(self, file_path: str) -> List[Task]:\n        tasks = []\n        try:\n            with open(file_path, 'r') as file:\n                for line in file:\n                    try:\n                        title, description = line.strip().split(',', 1)\n                        tasks.append(Task(title, description))\n                    except ValueError:\n                        print(f'Warning: Skipping malformed line: {line.strip()}')\n        except IOError as e:\n            print(f'An error occurred while loading tasks from file: {e}')\n        return tasks"
    },
    {
      "file_name": "cli.py",
      "code": "from todo_list_manager import ToDoListManager\nfrom task_model import Task\n\nclass CommandLineInterface:\n    def __init__(self):\n        self.manager = ToDoListManager()\n\n    def add_task(self, description):\n        task = Task(description)\n        self.manager.add_task(task)\n        return \"Task added successfully.\"\n\n    def remove_task(self, task_id):\n        if self.manager.delete_task(task_id):\n            return \"Task removed successfully.\"\n        else:\n            return \"Error: Task does not exist.\"\n\n    def process_command(self, command):\n        try:\n            command = command.strip().lower()\n            if command.startswith(\"add \"):\n                description = command[4:]\n                return self.add_task(description)\n            elif command.startswith(\"remove \"):\n                task_id = int(command[7:])\n                return self.remove_task(task_id)\n            else:\n                return \"Error: Unknown command. Please use 'add' or 'remove'.\"\n        except Exception as e:\n            return f\"An unexpected error occurred: {str(e)}\"\n\n    def run(self):\n        while True:\n            user_input = input(\"Enter command: \")\n            if user_input.lower() == \"exit\":\n                print(\"Exiting the program.\")\n                break\n            feedback = self.process_command(user_input)\n            print(feedback)"
    },
    {
      "file_name": "main_application.py",
      "code": "from cli import CommandLineInterface\n\ndef main_loop():\n    cli = CommandLineInterface()\n    cli.run()\n\nif __name__ == \"__main__\":\n    main_loop()"
    },
    {
      "file_name": "error_handling.py",
      "code": "class ErrorHandler:\n    def __init__(self):\n        pass\n\n    class InvalidDataTypeError(Exception):\n        pass\n\n    class OutOfRangeError(Exception):\n        pass\n\n    class MissingInputError(Exception):\n        pass\n\n    class FileNotFoundError(Exception):\n        pass\n\n    class PermissionDeniedError(Exception):\n        pass\n\n    class FileReadWriteError(Exception):\n        pass\n\n    def handle_input_error(self, error_type, value=None):\n        try:\n            if error_type == 'invalid_data_type':\n                raise self.InvalidDataTypeError(f\"Invalid data type provided: {value}. Please provide a valid data type.\")\n            elif error_type == 'out_of_range':\n                raise self.OutOfRangeError(f\"Value out of range: {value}. Please provide a value within the acceptable range.\")\n            elif error_type == 'missing_input':\n                raise self.MissingInputError(\"Required input is missing. Please provide all necessary inputs.\")\n        except (self.InvalidDataTypeError, self.OutOfRangeError, self.MissingInputError) as e:\n            return str(e)\n\n    def handle_file_error(self, error_type, file_path=None):\n        try:\n            if error_type == 'file_not_found':\n                raise self.FileNotFoundError(f\"File not found: {file_path}. Please check the file path and try again.\")\n            elif error_type == 'permission_denied':\n                raise self.PermissionDeniedError(f\"Permission denied for file: {file_path}. Please check your permissions.\")\n            elif error_type == 'file_read_write':\n                raise self.FileReadWriteError(f\"Error reading/writing file: {file_path}. Please check the file and try again.\")\n        except (self.FileNotFoundError, self.PermissionDeniedError, self.FileReadWriteError) as e:\n            return str(e)\n\nimport unittest\n\nclass TestErrorHandler(unittest.TestCase):\n    def setUp(self):\n        self.error_handler = ErrorHandler()\n\n    def test_invalid_data_type_error(self):\n        result = self.error_handler.handle_input_error('invalid_data_type', 'abc')\n        self.assertEqual(result, \"Invalid data type provided: abc. Please provide a valid data type.\")\n\n    def test_out_of_range_error(self):\n        result = self.error_handler.handle_input_error('out_of_range', 999)\n        self.assertEqual(result, \"Value out of range: 999. Please provide a value within the acceptable range.\")\n\n    def test_missing_input_error(self):\n        result = self.error_handler.handle_input_error('missing_input')\n        self.assertEqual(result, \"Required input is missing. Please provide all necessary inputs.\")\n\n    def test_file_not_found_error(self):\n        result = self.error_handler.handle_file_error('file_not_found', '/path/to/file')\n        self.assertEqual(result, \"File not found: /path/to/file. Please check the file path and try again.\")\n\n    def test_permission_denied_error(self):\n        result = self.error_handler.handle_file_error('permission_denied', '/path/to/file')\n        self.assertEqual(result, \"Permission denied for file: /path/to/file. Please check your permissions.\")\n\n    def test_file_read_write_error(self):\n        result = self.error_handler.handle_file_error('file_read_write', '/path/to/file')\n        self.assertEqual(result, \"Error reading/writing file: /path/to/file. Please check the file and try again.\")\n\nif __name__ == '__main__':\n    unittest.main()"
    }
  ]
    }

    create_python_files(data["integrated_files_list"])
