from typing import TypedDict
from src.utils import docraptor, templating, writer

out_dir = 'tests/out'

DocServiceArgs = TypedDict('DocServiceArgs', {
  "slug": str,
  "use_docraptor": bool,
  "test_mode": bool,
  "variables": dict,
})

DocServiceResult = TypedDict('DocServiceArgs', {
  "success": bool,
  "html": str,
  "pdf_bytes": bytes | None
})

# TODO: log which vars were and were not used when hydrating doc

def run_doc_service(args: DocServiceArgs) -> DocServiceResult:
  test_mode = args['test_mode']
  out_file_path = out_dir + '/' + args['slug']

  # render jinja template to html string
  html = templating.render_template(args)
  
  # optionally write html file (to preview in browser)
  if test_mode:
    writer.write_file(out_file_path + '.html', html)

  # create pdf in DocRaptor
  pdf_bytes = None
  
  if args['use_docraptor']:
    print('Creating PDF in DocRaptor...')
    pdf_bytes = docraptor.create_doc(
      file_name="My two page pdf",
      document_content=html
    )
    if test_mode:
      file_path = out_file_path + '.pdf'
      writer.write_file(file_path, pdf_bytes, 'wb')

  return {
    "success": True,
    "html": html,
    "pdf_bytes": pdf_bytes,
  }