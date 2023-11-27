import os
from dotenv import load_dotenv
import docraptor

load_dotenv()

docraptor_api_key = os.getenv('DOCRAPTOR_API_KEY')
doc_api = docraptor.DocApi()
doc_api.api_client.configuration.username = docraptor_api_key

response = doc_api.create_doc({
  "test": True,
  "document_content": "<html><body>Hello World</body></html>",
  "name": "docraptor-sandbox.pdf",
  "document_type": "pdf",
})

# ENV test