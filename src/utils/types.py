from typing import List, TypedDict, Required, Union

#####################
# COMMON BETWEEN DOCS

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

###################
# SPECIFIC DOC ARGS

# Adverse Advisor Notice

_AdverseAdvisorNoticeVars = TypedDict('AdverseAdvisorNoticeVars', {
  "date": str,
  "notice_date": str,
  "application_date": str,
  "credit_score": int | float,
  "adverse_action_notice_text": str,
  "key_factors": List[str],
})

AdverseAdvisorNoticeVars = Union[
  _AdverseAdvisorNoticeVars,
  Customer,
  PrimaryBorrower,
  CoBorrower,
  Lender
]

# Kitchen Sink

_KitchenSinkVars = TypedDict('KitchenSinkVars', {
  "date": str,
  "notice_date": str,
  "application_date": str,
  "credit_score": int | float,
  "intro": str,
  "list_of_things": List[str],
})

KitchenSinkVars = Union[
  _KitchenSinkVars,
  Customer,
  PrimaryBorrower,
  CoBorrower,
  Lender
]

DocVariables = AdverseAdvisorNoticeVars | KitchenSinkVars

##########
# DOC ARGS

Doc = TypedDict('Doc', {
  "slug": Required[str],
  "use_docraptor": bool,
  "test_mode": bool,
  "variables": DocVariables,
})

##################
# DOC SERVICE FUNC

DocServiceArgs = TypedDict('DocServiceArgs', {
  "slug": str,
  "use_docraptor": bool,
  "test_mode": bool,
  "variables": dict,
})

DocServiceResult = TypedDict('DocServiceArgs', {
  "success": bool,
  "html": str,
  "pdf_bytes": bytes | None,
})

