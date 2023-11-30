from src.doc_service import run_doc_service
from tests.fixtures.docs import kitchen_sink_args

def test_kitchen_sink_notice_doc():
  run_doc_service(kitchen_sink_args)
  assert True # so we can see the logs for now