from typing import TypedDict, Required

#################
# DOC ARGS COMMON

Customer = TypedDict('Customer', {
  "customer_file_number": Required[str],
})

PrimaryBorrower = TypedDict('PrimaryBorrower', {
  "primary_borrower_full_name": Required[str],
  "primary_borrower_address": Required[str],
})

CoBorrower = TypedDict('CoBorrower', {
  "co_borrower_full_name": Required[str],
  "co_borrower_address": Required[str],
})

Lender = TypedDict('Lender', {
  "lender_name": Required[str],
  "lender_address": Required[str],
  "lender_phone": Required[str],
  "lender_website": Required[str],
  "lender_originator": Required[str],
  "lender_originator_nmls": Required[str],
  "lender_logo": str,
})

Doc = TypedDict('Doc', {
  
})

###################
# DOC ARGS SPECIFIC




# TODO...

#############
# DOC SERVICE

DocServiceArgs = TypedDict('DocServiceArgs', {
  "slug": str,
  "use_docraptor": bool,
  "test_mode": bool,
  "variables": dict,
})

DocServiceResult = TypedDict('DocServiceArgs', {
  "success": bool,
  "html": str,
  "pdf_bytes": bytes | None
})

