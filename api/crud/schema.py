from typing import Optional
from pydantic import BaseModel

class GetData(BaseModel):
    data_id: Optional[str]
    data_name: Optional[str]
    data_description: Optional[str]

class CreateData(BaseModel):
    data_name: str
    data_description: str

class UpdateData(BaseModel):
    data_id: str
    data_name: Optional[str]
    data_description: Optional[str]