SHELL = /bin/bash
ENV = env
BIN = $(ENV)/bin
PIP = $(BIN)/pip

default: testing

testing: install-requirements install-requirements-testing activate

production: install-requirements activate

install-requirements: virtualenv
	$(PIP) install -r requirements.txt

install-requirements-testing: install-requirements
	$(PIP) install -r requirements-testing.txt

virtualenv:
	virtualenv $(ENV)

activate:
	source $(BIN)/activate

test:
	bin/py.test -m 'not ignore' --pep8 tests

clean:
	rm -Rf $(ENV)
