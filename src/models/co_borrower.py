from pydantic import BaseModel

class CoBorrower(BaseModel):
  co_borrower_full_name: str
  co_borrower_address: str
