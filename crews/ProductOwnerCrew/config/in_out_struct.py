from pydantic import BaseModel, Field
from typing import Dict, Optional, List, Set, Tuple


class SoftwareComponent(BaseModel):
    software_component_type: str = Field(..., description="The type of the software component to be implemented, can be a function, class, etc.")
    software_component_name: str = Field(..., description="The name of the software component to be implemented.")
    inputs: Dict[str, str] = Field(..., description="The inputs required to implement the software component.")
    outputs: Dict[str, str] = Field(..., description="The outputs of the software component.")
    requirements: str = Field(..., description="The requirements of the software component.")
    methods: Dict[str, str] = Field(..., description="The methods to be implemented in the software component.")
    description: str = Field(..., description="The description of the software component.")
    dependencies: str = Field(..., description="The dependencies of the software component like includes or imports.")
    project_integration_considerations: str = Field(..., description="The project's integration considerations of the software component.")
    break_down_of_project: str = Field(..., description="The break down of the full project.")


class SoftwareFile(BaseModel):
    file_name: str = Field(..., description="The name of the file.")
    file_purpose: str = Field(..., description="The purpose of the file.")
    software_component: SoftwareComponent = Field(..., description="The software components to be implemented in the file.")

class SoftwareFilesList(BaseModel):
    software_files_list: List[SoftwareFile] = Field(..., description="The list of software files.")