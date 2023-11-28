import sys
from src.utils import docraptor, templating, writer

out_dir = 'out'

# render an html template
html = templating.render_template()

# write file (to preview in browser)
writer.write_file(out_dir + '/index.html', html)

# create pdf in DocRaptor
if len(sys.argv) > 1 and sys.argv[1] == '--docraptor':
  print('Creating PDF in DocRaptor...')
  pdf_string = docraptor.create_doc(
    file_name="My two page pdf",
    document_content=html
  )
  file_path = out_dir + '/test.pdf'
  writer.write_file(file_path, pdf_string, 'wb')