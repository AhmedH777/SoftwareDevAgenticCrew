from pydantic import BaseModel, Field
from typing import Dict, Optional, List, Set, Tuple


class IntegratedFiles(BaseModel):
    file_name: str = Field(..., description="Name of the file.")
    code: str = Field(..., description="Integrated code.")

class IntegratedFilesList(BaseModel):
    integrated_files_list: List[IntegratedFiles] = Field(..., description="List of integrated files.")

