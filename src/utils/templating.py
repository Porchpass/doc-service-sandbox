from typing import TypedDict
from jinja2 import Environment, FileSystemLoader, select_autoescape

# configure jinja
template_loader = FileSystemLoader('src/templates')

env = Environment(
  loader=template_loader,
  autoescape=select_autoescape()
)

RenderTemplateArgs = TypedDict('RenderTemplateArgs', {
  "title": str,
  "slug": str,
  "variables": dict
})

# main method
def render_template(args: RenderTemplateArgs):
  print('ARGS')
  print(args['title'])
  template = env.get_template(args['slug'] + '.html.jinja')
  html = template.render({ "title": args['title'], **args['variables'] })
  return html