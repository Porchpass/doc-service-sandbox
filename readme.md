# DocRaptor Sandbox

A DocGen service using [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/api/#basics) templating and [DocRaptor](https://docraptor.com/documentation/pdf_generation/reference) PDF generation. 

## Usage

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

## Dev Setup

Install [Virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html) and set up an environment:

`virtualenv .venv`

Make sure to activate it (Mac / Linux):

`source .venv/bin/activate`

Add ENV vars.

Create the file `cp .env.sample .env` and enter the values.

Install packages

`pip3 install -r requirements.txt`

## Testing

Run `pytest` from the root of the project.

### Previewing HTML

You can serve the html output locally by running `python3 -m http.server -d ./tests/out` and navigating to the file in in the browser.

**NOTE:** ~~When looking at the HTML, the footer will be the first element you see, above the rest of the content. DocRaptor requires the repeated `headers` and `footers` to be output first in the markup. See [https://docraptor.com/documentation/article/1067094-headers-footers](https://docraptor.com/documentation/article/1067094-headers-footers) for more info.~~ 👈 We are now using multiple header/footer partials per doc instead of DocRaptor's header/footer functionality.

## Helpful links

* https://pip.pypa.io/en/stable/user_guide/
* https://pypi.org/project/pipx/
* https://virtualenv.pypa.io/en/latest/user_guide.html
* https://jinja.palletsprojects.com/en/3.1.x/api/#basics
* https://stackoverflow.com/questions/71015047/how-to-use-jinja-to-render-html-without-flask
* https://docraptor.com/documentation/pdf_generation/reference

<!-- figma links -->
<!-- https://www.figma.com/file/WD0gPOMPNUOqF1NQWrKVdI/Document-Templates?type=design&node-id=212-2&mode=design&t=dtQOKwUTv0P1yMAj-0 -->
<!-- https://www.figma.com/file/WD0gPOMPNUOqF1NQWrKVdI/Document-Templates?type=design&node-id=373-693&mode=design&t=PmCa8As5d19F5LfH-0 -->