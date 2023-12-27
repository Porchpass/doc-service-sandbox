from typing import List
from pydantic import BaseModel
from src.models import Customer, PrimaryBorrower, CoBorrower, Lender

class AdverActionNoticeVars(BaseModel):
  date: str
  notice_date: str
  application_date: str
  credit_score: int | float
  adverse_action_notice_text: str
  key_factors: List[str]
  customer: Customer
  primary_borrower: PrimaryBorrower
  co_borrower: CoBorrower
  lender: Lender