from typing import Any, Literal, Optional
from pydantic import BaseModel

# response schemas
class StandardResponse(BaseModel):
    status: str
    status_code: Optional[int] = 200
    message: Optional[str]

class GetResponse(BaseModel):
    status: str
    status_code: Optional[int] = 200
    data: Optional[Any] = []
    total_rows: Optional[int] = 0


