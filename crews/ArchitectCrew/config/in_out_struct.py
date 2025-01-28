from pydantic import BaseModel, Field
from typing import Dict, Optional, List, Set, Tuple


class ArchitectureBlock(BaseModel):
    block_name: str = Field(..., description="Given name of the block.")
    description: str = Field(..., description="Description of the block.")
    dependencies: str = Field(..., description="Dependencies of the block.")
    input_list : List[str] = Field(..., description="List of inputs to the block.")
    output_list : List[str] = Field(..., description="List of outputs from the block.")

class Architecture(BaseModel):
    architecture_name: str = Field(..., description="Given name of the architecture.")
    description: str = Field(..., description="Description of the architecture.")
    architect_comments: str = Field(..., description="Comments from the architect.")
    architecture_blocks : List[ArchitectureBlock]

