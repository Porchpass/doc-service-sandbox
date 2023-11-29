from typing import TypedDict
from src.utils import docraptor, templating, writer

DocServiceArgs = TypedDict('DocServiceArgs', {
  "slug": str,
  "use_docraptor": bool,
  "variables": dict,
  "test_mode": True
})

def run_doc_service(args: DocServiceArgs):
  
#   # render an html template
#   html = templating.render_template()

#   # write file (to preview in browser)
#   writer.write_file(out_dir + '/index.html', html)

#   # create pdf in DocRaptor
#   if len(sys.argv) > 2 and sys.argv[2] == '--docraptor':
#     print('Creating PDF in DocRaptor...')
#     pdf_bytes = docraptor.create_doc(
#       file_name="My two page pdf",
#       document_content=html
#     )
#     file_path = out_dir + '/test.pdf'
#     writer.write_file(file_path, pdf_bytes, 'wb')
