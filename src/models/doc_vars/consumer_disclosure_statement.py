from pydantic import BaseModel
from src.models import Lender

class ConsumerDisclosureStatementVars(BaseModel):
  dealer_name: str
  lender: Lender