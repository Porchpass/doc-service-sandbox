from pydantic import BaseModel

class Person(BaseModel):
  full_name: str
  