from typing import Optional
from pydantic import BaseModel, UUID4

class GetData(BaseModel):
    data_id: Optional[UUID4]
    data_name: Optional[str]
    data_description: Optional[str]

class CreateData(BaseModel):
    data_name: str
    data_description: str

class UpdateData(BaseModel):
    data_id: UUID4
    data_name: Optional[str]
    data_description: Optional[str]