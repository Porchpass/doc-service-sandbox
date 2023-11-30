from src.doc_service import DocServiceArgs, DocServiceResult

def assert_doc_service_result(args: DocServiceArgs, result: DocServiceResult):
  # did the service run successfully?
  assert result['success'] == True
  # Do we have an HTML string?
  assert type(result['html']) is str
  # if using DocRaptor, did we receive pdf bytes
  if args['use_docraptor']:
    assert type(result['pdf_bytes']) is bytes
  else:
    assert result['pdf_bytes'] == None