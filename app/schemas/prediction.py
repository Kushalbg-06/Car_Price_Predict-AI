from pydantic import BaseModel

class CarInput(BaseModel):
    year: int
    km_driven: int
    fuel: str
    transmission: str
    owner: str
    company: str