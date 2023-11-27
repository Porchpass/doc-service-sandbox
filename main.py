import docraptor

doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = '' # api key

response = doc_api.create_doc({
  "test": True,
  "document_content": "<html><body>Hello World</body></html>",
  "name": "docraptor-sandbox.pdf",
  "document_type": "pdf",
})