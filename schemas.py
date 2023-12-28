from pydantic import BaseModel, Field , validator
from typing import List
import re

class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currenies: List[str]

    @validator('to_currenies')
    def validate_to_currenies(cls,value):
        for courrency in value:
            if not re.match('^[A-Z]{3}$',courrency):
                raise ValueError(f'Invalid currency {courrency}')
        return value
    class Config:
        arbitrary_types_allowed = True

class ConverterOutput(BaseModel):
    message: str
    data: List[dict]
    class Config:
        arbitrary_types_allowed = True
        