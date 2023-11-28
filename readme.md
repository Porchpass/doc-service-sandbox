# DocRaptor Sandbox

Trying out [DocRaptor](https://docraptor.com/documentation/pdf_generation/reference) and [Jinja](https://jinja.palletsprojects.com/en/3.1.x/api/#basics) templating.

## Setup

Install [Virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html) and set up an environment:

`virtualenv .venv`

Make sure to activate it (Mac / Linux):

`source .venv/bin/activate`

Add ENV vars.

Create the file `cp .env.sample .env` and enter the values.

Install packages

`pip3 install -r requirements.txt`

## Compile template

Use the optional `--docraptor` arg to create PDF in DocRaptor and save the result to your local machine.

`python3 main.py --docraptor`

## HTML Preview

`python3 -m http.server -d ./out` and open in the browser.

## Helpful links

* https://pip.pypa.io/en/stable/user_guide/
* https://pypi.org/project/pipx/
* https://virtualenv.pypa.io/en/latest/user_guide.html
* https://jinja.palletsprojects.com/en/3.1.x/api/#basics
* https://stackoverflow.com/questions/71015047/how-to-use-jinja-to-render-html-without-flask
* https://docraptor.com/documentation/pdf_generation/reference
* https://jenil.github.io/chota/