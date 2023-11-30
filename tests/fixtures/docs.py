from tests.fixtures.common import (
  fake_customer, 
  fake_primary_borrower, 
  fake_co_borrower, 
  fake_lender
)

# devs: flip these settings to test different situations
test_mode = True # should we write html files to fs?
use_docraptor = False # should we generate PDF through DocRaptor?

adverse_advisor_notice_args = {
  "slug": "adverse_action_notice",
  "use_docraptor": use_docraptor,
  "test_mode": test_mode,
  "variables": {
    "date": "10/9/2024",
    "notice_date": "10/10/2024",
    "credit_score": 3,
    "adverse_action_notice_text": "This is some test advisor notice text...",
    **fake_customer,
    **fake_primary_borrower,
    **fake_co_borrower,
    **fake_lender,
  },
}

kitchen_sink_args = {
  "slug": "kitchen_sink",
  "use_docraptor": use_docraptor,
  "test_mode": test_mode,
  "variables": {
    "date": "10/9/2024",
    "notice_date": "10/10/2024",
    "credit_score": 7,
    "list_of_things": [
      'Item 1',
      'Item 2', 
      'Item 3'
    ],
    **fake_customer,
    **fake_primary_borrower,
    **fake_co_borrower,
    **fake_lender,
  },
}