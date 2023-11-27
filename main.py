############
# Jinja test

from jinja2 import Environment, FileSystemLoader, select_autoescape

template_loader = FileSystemLoader('templates')
env = Environment(
  loader=template_loader,
  autoescape=select_autoescape()
)

template = env.get_template('index.html.jinja')
html = template.render(name="Jinja2")

print(html)

################
# DocRaptor test

# import os
# from dotenv import load_dotenv
# import docraptor

# load_dotenv()

# docraptor_api_key = os.getenv('DOCRAPTOR_API_KEY')
# doc_api = docraptor.DocApi()
# doc_api.api_client.configuration.username = docraptor_api_key

# response = doc_api.create_doc({
#   "test": True,
#   "document_content": "<html><body>Hello World</body></html>",
#   "name": "docraptor-sandbox.pdf",
#   "document_type": "pdf",
# })