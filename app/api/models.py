from pydantic import BaseModel
from typing import List, Optional

class EmployeeIn(BaseModel):
    name: str
    surname: str
    age: int
    phone: str


class EmployeeOut(EmployeeIn):
    id: int
