from src.doc_service import run_doc_service
from tests.fixtures.docs import adverse_advisor_notice_args
from tests.utils.helpers import assert_doc_service_result

def test_adverse_advisor_notice_doc():
	result = run_doc_service(adverse_advisor_notice_args)
	assert_doc_service_result(adverse_advisor_notice_args, result)