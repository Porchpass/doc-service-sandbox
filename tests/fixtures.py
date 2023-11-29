########
# common

fake_customer = {
  "customer_file_number": "1234567",
}

fake_primary_borrower = {
  "primary_borrower_full_name": "TestPri P. Borrower",
  "primary_borrower_address": "123 P Borrow Blvd, City, State 00000",
}

fake_co_borrower = {
  "primary_borrower_full_name": "TestCo Co. Borrower",
  "primary_borrower_address": "123 Co Borrow Blvd, City, State 00000",
}

fake_lender = {
  "lender_name": "Test Lender",
  "lender_address": "123 Lender St, City, State 00000",
  "lender_phone": "1-800-LENDER",
  "lender_website": "https://lender.com",
  "lender_originator": "Lender Originator Name",
  "lender_originator_nmls": "NMLS-000000",
  "lender_logo": "https://placehold.co/600x400"
}

###############
# Doc variables

adverse_advisor_notice_args = {
  "slug": "adverse_action_notice",
  "use_docraptor": False,
  "test_mode": True,
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