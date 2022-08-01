.PHONY: virtual install flake8 run

virtual: .venv/bin/pip # Creates an isolated python 3 environment

.venv/bin/pip:
	python3 -m venv .venv

install: virtual
	.venv/bin/pip install -Ur requirements.txt
	.venv/bin/python3 manage.py migrate
	
update-requirements: install
	.venv/bin/pip freeze > requirements.txt

flake8:  # Lints code using flake8
	.venv/bin/flake8 api/*.py
	.venv/bin/flake8 authentication/*.py
	.venv/bin/flake8 stock_market/*.py

run:
	.venv/bin/python3 manage.py runserver