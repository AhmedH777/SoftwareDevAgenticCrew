from pydantic import BaseModel, Field
from typing import Dict, Optional, List, Set, Tuple


class SoftwareFile(BaseModel):
    software_file_name: str = Field(..., description="The name of the software file.")
    software_file_implmentation: str = Field(..., description="The implementation of the software file.")