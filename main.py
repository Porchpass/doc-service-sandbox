from src.utils import docraptor, templating, writer

# render an html template
html = templating.render_template()

# write file (to preview in browser)
file_path = 'out/index.html'
writer.write_file(file_path, html)

# create pdf in DocRaptor
# response = docraptor.create_doc(
  # TODO: add args
# )
# print(response)