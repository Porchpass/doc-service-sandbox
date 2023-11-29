from src.doc_service import run_doc_service
from tests.fixtures import adverse_advisor_notice_args

def test_adverse_advisor_notice_doc():
    run_doc_service(adverse_advisor_notice_args)
    assert False # so we can see the logs for now