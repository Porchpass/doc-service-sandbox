import os
from dotenv import load_dotenv
import docraptor

load_dotenv()

# ensure we have an API key
docraptor_api_key = os.getenv('DOCRAPTOR_API_KEY', None)
if not docraptor_api_key: 
  raise Exception("missing DOCRAPTOR_API_KEY")

# configure DocRaptor
doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = docraptor_api_key

def create_doc(
  file_name: str = "docraptor-sandbox",
  document_content: str = "<html><body>Hello World</body></html>",
  document_type: str = "pdf",
  test: bool = True,
):
  result = None 
  try:
    result = doc_api.create_doc({
      "name": file_name + ".pdf",
      "document_content": document_content, 
      "document_type": document_type,
      "test": test,
    })
  except:
    print(result)
    raise Exception('☝ Error creating doc in DocRaptor')
  else:
    return result