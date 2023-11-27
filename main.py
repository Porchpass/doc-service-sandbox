from src.utils import docraptor, templating

# render an html template
html = templating.render_template()

# write file (to preview in browser)
file_path = 'out/index.html'
f = open(file_path, 'w')
f.write(html)
f.close()
print('file written to ' + file_path)

# create pdf in DocRaptor
# response = docraptor.create_doc()
# print(response)