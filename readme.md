# DocRaptor Sandbox

A repo to play around with DocRaptor.

## Setup

Install Virtualenv.

* https://pip.pypa.io/en/stable/user_guide/
* https://pypi.org/project/pipx/
* https://virtualenv.pypa.io/en/latest/user_guide.html

Set up a virtual environment. 

`virtualenv .venv`

Make sure to activate it (Mac / Linux). 

`source .venv/bin/activate`

Add ENV vars. Create the file and go add the values.

`cp .env.sample .env`

Install packages

`pip3 install -r requirements.txt`

## Run

`python3 main.py`