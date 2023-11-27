from jinja2 import Environment, FileSystemLoader, select_autoescape

template_loader = FileSystemLoader('templates')
env = Environment(
  loader=template_loader,
  autoescape=select_autoescape()
)

def render_template():
  template = env.get_template('index.html.jinja')
  return template.render(name="Jinja2")