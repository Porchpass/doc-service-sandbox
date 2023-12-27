from pydantic import BaseModel

class Customer(BaseModel):
  customer_file_number: str
  full_name: str