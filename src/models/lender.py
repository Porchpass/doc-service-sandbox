from pydantic import BaseModel

class Lender(BaseModel):
  lender_name: str
  lender_address: str
  lender_phone: str
  lender_website: str
  lender_originator: str
  lender_originator_nmls: str
  lender_logo: str