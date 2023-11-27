from jinja2 import Environment, FileSystemLoader, select_autoescape

template_loader = FileSystemLoader('templates')

env = Environment(
  loader=template_loader,
  autoescape=select_autoescape()
)

def render_template(
  template_file_slug: str = 'test-doc.html.jinja',
  title: str = 'Jinja2',
):
  template = env.get_template(template_file_slug)
  html = template.render(
    title=title,
  )
  return html