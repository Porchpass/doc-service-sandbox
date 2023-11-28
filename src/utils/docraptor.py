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
  file_name: str,
  document_content: str,
  document_type: str = "pdf",
  test: bool = True,
):
  if not file_name:
    raise Exception("create_doc missing file_name")
  if not document_content:
    raise Exception("create_doc missing document_content")
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