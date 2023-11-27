from src.utils import docraptor, templating

# render an html template
html = templating.render_template()

# write file (to preview in browser)
f = open('temp.html', 'w')
f.write(html)
f.close()
print('temp.html file written')

# create pdf in DocRaptor
# response = docraptor.create_doc()
# print(response)