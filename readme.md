# DocRaptor Sandbox

Trying out [DocRaptor](https://docraptor.com/documentation/pdf_generation/reference) and [Jinja](https://jinja.palletsprojects.com/en/3.1.x/api/#basics) templating.

## Dev Setup

Install [Virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html) and set up an environment:

`virtualenv .venv`

Make sure to activate it (Mac / Linux):

`source .venv/bin/activate`

Add ENV vars.

Create the file `cp .env.sample .env` and enter the values.

Install packages

`pip3 install -r requirements.txt`

## Future Usage by consumers

```py
from src.doc_service import run_doc_service # TODO: how to make this import cleaner?

result = run_doc_service({
  "slug": str,
  "use_docraptor": bool,
  "test_mode": bool,
  "variables": dict,
})

# Returns:
# {
#   "success": bool,
#   "html": str,
#   "pdf_bytes": bytes | None
# }  
```

## Testing

Run `pytest` then go check the `out` directory for your html and pdfs.

## Previewing HTML

You can serve the html output locally by running `python3 -m http.server -d ./out` and navigating to the file in in the browser. 

Just remember that the footer will be the first element. See: [https://docraptor.com/documentation/article/1067094-headers-footers](https://docraptor.com/documentation/article/1067094-headers-footers)

## Helpful links

* https://pip.pypa.io/en/stable/user_guide/
* https://pypi.org/project/pipx/
* https://virtualenv.pypa.io/en/latest/user_guide.html
* https://jinja.palletsprojects.com/en/3.1.x/api/#basics
* https://stackoverflow.com/questions/71015047/how-to-use-jinja-to-render-html-without-flask
* https://docraptor.com/documentation/pdf_generation/reference

<!-- https://www.figma.com/file/WD0gPOMPNUOqF1NQWrKVdI/Document-Templates?type=design&node-id=212-2&mode=design&t=dtQOKwUTv0P1yMAj-0 -->
<!-- https://www.figma.com/file/WD0gPOMPNUOqF1NQWrKVdI/Document-Templates?type=design&node-id=373-693&mode=design&t=PmCa8As5d19F5LfH-0 -->