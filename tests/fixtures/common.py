from src.utils.types import Customer, PrimaryBorrower, CoBorrower, Lender

fake_customer: Customer = {
  "customer_file_number": "1234567",
}

fake_primary_borrower: PrimaryBorrower = {
  "primary_borrower_full_name": "TestPri P. Borrower",
  "primary_borrower_address": "123 P Borrow Blvd, City, State 00000",
}

fake_co_borrower: CoBorrower = {
  "co_borrower_full_name": "TestCo Co. Borrower",
  "co_borrower_address": "123 Co Borrow Blvd, City, State 00000",
}

fake_lender: Lender = {
  "lender_name": "Test Lender",
  "lender_address": "123 Lender St, City, State 00000",
  "lender_phone": "1-800-LENDER",
  "lender_website": "https://lender.com",
  "lender_originator": "Lender Originator Name",
  "lender_originator_nmls": "NMLS-000000",
  "lender_logo": "https://placehold.co/600x400"
}