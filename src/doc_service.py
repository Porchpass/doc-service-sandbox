from typing import TypedDict
from src.utils import docraptor, templating, writer

out_dir = 'out'

DocServiceArgs = TypedDict('DocServiceArgs', {
  "slug": str,
  "use_docraptor": bool,
  "test_mode": bool,
  "variables": dict,
})

def run_doc_service(args: DocServiceArgs):
  # render jinja template to html string
  html = templating.render_template(args)
  print(html)

  if args['test_mode']:
    # write file (to preview in browser)
    writer.write_file(out_dir + '/' + args['slug'] + '.html', html)

#   # create pdf in DocRaptor
#   if len(sys.argv) > 2 and sys.argv[2] == '--docraptor':
#     print('Creating PDF in DocRaptor...')
#     pdf_bytes = docraptor.create_doc(
#       file_name="My two page pdf",
#       document_content=html
#     )
#     file_path = out_dir + '/test.pdf'
#     writer.write_file(file_path, pdf_bytes, 'wb')
