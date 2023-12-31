from src.utils.types import Doc, AdverseAdvisorNoticeVars, ConsumerDisclosureStatementVars, KitchenSinkVars
from tests.fixtures.common import (
  fake_customer, 
  fake_primary_borrower, 
  fake_co_borrower, 
  fake_lender
)

# devs: flip these settings to test different situations
test_mode = True # should we write html files to fs?
use_docraptor = True # should we generate PDF through DocRaptor?

#######################
# Adverse Action Notice

adverse_action_notice_variables: AdverseAdvisorNoticeVars = {
  "date": "10/9/2024",
  "notice_date": "10/10/2024",
  "application_date": "10/10/2024",
  "credit_score": 3,
  "adverse_action_notice_text": "This is some test advisor notice text...",
  "key_factors": [
    "This is one reason",
    "Here are 2 more reasons",
    "Three reasons is a lot already",
    "There's a fourth reason?!",
    "This is the last reason",
  ],
  **fake_customer,
  **fake_primary_borrower,
  **fake_co_borrower,
  **fake_lender,
}

adverse_action_notice_args: Doc = {
  "slug": "adverse_action_notice",
  "use_docraptor": use_docraptor,
  "test_mode": test_mode,
  "variables": adverse_action_notice_variables,
}

###############################
# Consumer Disclosure Statement

consumer_disclosure_statement_args_variables: ConsumerDisclosureStatementVars = {
  "dealer_name": "My Test Dealer",
  **fake_lender,
}

consumer_disclosure_statement_args: Doc = {
  "slug": "consumer_disclosure_statement",
  "use_docraptor": use_docraptor,
  "test_mode": test_mode,
  "variables": consumer_disclosure_statement_args_variables,
}

##############
# Kitchen Sink

kitchen_sink_args: KitchenSinkVars = {
  "date": "10/9/2024",
  "notice_date": "10/10/2024",
  "credit_score": 7,
  "intro": "This entire paragraph is dynamically inserted! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
  "list_of_things": [
    'Item 1',
    'Item 2', 
    'Item 3'
  ],
  **fake_customer,
  **fake_primary_borrower,
  **fake_co_borrower,
  **fake_lender,
}

kitchen_sink_args: Doc = {
  "slug": "kitchen_sink",
  "use_docraptor": use_docraptor,
  "test_mode": test_mode,
  "variables": kitchen_sink_args,
}