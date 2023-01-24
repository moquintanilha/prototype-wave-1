from pydantic import BaseModel


class People(BaseModel):
    name: str
    birth_date: str
    country: str
