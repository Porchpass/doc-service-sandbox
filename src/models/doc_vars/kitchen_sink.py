from typing import List
from pydantic import BaseModel
from src.models import Customer, PrimaryBorrower, CoBorrower, Lender

class KitchenSinkVars(BaseModel):
  date: str
  notice_date: str
  application_date: str
  credit_score: int | float
  intro: str
  list_of_things: List[str]
  customer: Customer
  primary_borrower: PrimaryBorrower
  co_borrower: CoBorrower
  lender: Lender