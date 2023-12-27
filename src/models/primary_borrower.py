from pydantic import BaseModel

class PrimaryBorrower(BaseModel):
  primary_borrower_full_name: str
  primary_borrower_address: str
