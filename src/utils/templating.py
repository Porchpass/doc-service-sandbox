from typing import TypedDict
from jinja2 import Environment, FileSystemLoader, select_autoescape

# configure jinja
template_loader = FileSystemLoader('src/templates')

env = Environment(
  loader=template_loader,
  autoescape=select_autoescape()
)

RenderTemplateArgs = TypedDict('RenderTemplateArgs', {
  "slug": str,
  "variables": dict
})

# main method
def render_template(args: RenderTemplateArgs) -> str:
  template = env.get_template(args['slug'] + '.html.jinja')
  html = template.render(args['variables'])
  return html