from pydantic import BaseModel, computed_field
from src.models.person import Person

class Customer(Person):
  
  customer_file_number: str
  customer_full_name: str
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.customer_full_name = self.full_name

  # @computed_field
  # def _create_customer_full_name(self):
  #   self.customer_full_name = self.full_name
    