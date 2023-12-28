from typing import List, TypedDict, Union

#####################
# COMMON BETWEEN DOCS

Customer = TypedDict('Customer', {
  "customer_file_number": str,
})

PrimaryBorrower = TypedDict('PrimaryBorrower', {
  "primary_borrower_full_name": str,
  "primary_borrower_address": str,
})

CoBorrower = TypedDict('CoBorrower', {
  "co_borrower_full_name": str,
  "co_borrower_address": str,
})

Lender = TypedDict('Lender', {
  "lender_name": str,
  "lender_address": str,
  "lender_phone": str,
  "lender_website": str,
  "lender_originator": str,
  "lender_originator_nmls": str,
  "lender_logo": str,
})

###################
# SPECIFIC DOC ARGS

# Adverse Advisor Notice

_AdverseAdvisorNoticeVars = TypedDict('_AdverseAdvisorNoticeVars', {
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

# Consumer Disclosure Statement

_ConsumerDisclosureStatementVars = TypedDict('_ConsumerDisclosureStatement', {
  "dealer_name": str
})

ConsumerDisclosureStatementVars = Union[_ConsumerDisclosureStatementVars, Lender]

# Kitchen Sink

_KitchenSinkVars = TypedDict('_KitchenSinkVars', {
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

DocVariables = AdverseAdvisorNoticeVars | ConsumerDisclosureStatementVars | KitchenSinkVars

##########
# DOC ARGS

Doc = TypedDict('Doc', {
  "slug": str,
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

