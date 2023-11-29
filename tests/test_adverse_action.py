from src.doc_service import run_doc_service
from tests.fixtures import fake_customer, fake_primary_borrower, fake_co_borrower, fake_lender

args = {
  "slug": "adverse_action",
  "use_docraptor": False,
  "variables": {
    "date": "10/9/2024",
    "notice_date": "10/10/2024",
    "credit_score": 3,
    **fake_customer,
    **fake_primary_borrower,
    **fake_co_borrower,
    **fake_lender,
  },
  "test_mode": True
}

def test_answer():
    run_doc_service(args)
    
    
    assert False # so we can see the logs for now