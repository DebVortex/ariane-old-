BUILDDIR ?= _build
ENV ?= dev
PORT ?= 8000
SPHINXOPTS =

define CMDS
ifeq ($(1), runserver)
	envdir envs/$(ENV) ariane/manage.py$(1)$(PORT)
else
$(1):
	envdir envs/$(ENV) ariane/manage.py$(1)
endif
endef

$(eval $(call CMDS, $(cmd)))

.PHONY: help clean clean-build clean-docs clean-pyc clean-test cmd compile-vendor coverage \
	coverage-html coverage-js coverage-js-html create-db develop docs isort migrate open-docs \
	serve-docs runserver shell startapp test test-all test-js test-upload upload

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean                    to remove all build, test, coverage and Python artifacts (does not remove backups)"
	@echo "  clean-backups            to remove backup files created by editors and Git"
	@echo "  clean-build              to remove build artifacts"
	@echo "  clean-docs               to remove documentation artifacts"
	@echo "  clean-pyc                to remove Python file artifacts"
	@echo "  clean-test               to remove test and coverage artifacts"
	@echo "  cmd=<manage.py command>  to use any other manage.py command"
	@echo "  compile-scss             to compile the scss files into a single css file."
	@echo "  compile-vendor           to compile and copy vendor javascript"
	@echo "  coverage                 to generate a coverage report with the default Python"
	@echo "  coverage-html            to generate and open a HTML coverage report with the default Python"
	@echo "  coverage-js              to generate a coverage report for the javascript"
	@echo "  coverage-js-html         to generate and open a HTML coverage report for the javascript"
	@echo "  create-db                to create a new PostgreSQL database"
	@echo "  create-db-user           to create a new PostgreSQL user"
	@echo "  drop-db                  to drop the PostgreSQL database"
	@echo "  drop-db-user             to drop the PostgreSQL user"
	@echo "  develop                  to install (or update) all packages required for development"
	@echo "  dist                     to package a release"
	@echo "  docs                     to build the project documentation as HTML"
	@echo "  isort                    to run isort on the whole project"
	@echo "  migrate                  to synchronize Django's database state with the current set of models and migrations"
	@echo "  open-docs                to open the project documentation in the default browser"
	@echo "  runserver                to start Django's development Web server"
	@echo "  serve-docs               to serve the project documentation in the default browser"
	@echo "  shell                    to start a Python interactive interpreter"
	@echo "  startapp                 to create a new Django app"
	@echo "  test                     to run unit tests quickly with the default Python"
	@echo "  test-all                 to run javascript unit test and unit tests on every Python version with tox"
	@echo "  test-upload              to upload a release to test PyPI using twine"
	@echo "  upload                   to upload a release using twine"


clean: clean-build clean-docs clean-test clean-pyc

clean-backups:
	find . -name '*~' -delete
	find . -name '*.orig' -delete
	find . -name '*.swp' -delete

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-docs:
	$(MAKE) -C docs clean BUILDDIR=$(BUILDDIR)

clean-pyc:
	find . -name '*.pyc' -delete
	find . -name '*.pyo' -delete
	find . -name '__pycache__' -delete

clean-test:
	rm -fr .cache/
	rm -fr .tox/
	coverage erase
	rm -fr htmlcov/

cmd:
	@echo "  cmd                       Please use 'make cmd=<manage.py command>'"

compile-scss:
	node_modules/.bin/grunt sass

compile-vendor:
	node_modules/.bin/modernizr -c node_modules/modernizr/lib/config-all.json -d node_modules/modernizr/
	node_modules/.bin/grunt uglify

coverage:
	envdir envs/$(ENV) coverage run -m pytest $(TEST_ARGS) tests/
	coverage report

coverage-html: coverage
	coverage html
	python -c "import os, webbrowser; webbrowser.open('file://{}/htmlcov/index.html'.format(os.getcwd()))"

coverage-js:
	npm test

coverage-js-html: coverage-js
	python -c "import os, webbrowser; webbrowser.open('file://{}/jsreport/html-coverage/index.html'.format(os.getcwd()))"

create-db:
	envdir envs/$(ENV) createdb -U ariane -l en_US.utf-8 -E utf-8 -O ariane -T template0 -e ariane

create-db-user:
	psql -d postgres -c "CREATE USER \"ariane\" WITH PASSWORD 'ariane' CREATEDB;"

drop-db:
	envdir envs/$(ENV) dropdb -i -e -U ariane ariane

drop-db-user:
	dropuser -i -e ariane

develop:
	pip install -U pip setuptools wheel
	pip install -U -c requirements/constraints.pip -e .
	pip install -U -c requirements/constraints.pip -r requirements/dev.pip
	npm install

dist: clean
	python setup.py sdist bdist_wheel
	ls -l dist

docs:
	$(MAKE) -C docs html BUILDDIR=$(BUILDDIR) SPHINXOPTS='$(SPHINXOPTS)'

isort:
	isort --recursive setup.py ariane/ tests/

migrate:
	envdir envs/$(ENV) python manage.py migrate

open-docs:
	python -c "import os, webbrowser; webbrowser.open('file://{}/docs/{}/html/index.html'.format(os.getcwd(), '$(BUILDDIR)'))"

runserver:
	envdir envs/$(ENV) python manage.py runserver $(PORT)

serve-docs:
	python -c "import webbrowser; webbrowser.open('http://127.0.0.1:$(PORT)')"
	cd docs/$(BUILDDIR)/html; python -m http.server $(PORT)

shell:
	envdir envs/$(ENV) python manage.py shell

startapp:
	@read -p "Enter the name of the new Django app: " app_name; \
	app_name_title=`python -c "import sys; sys.stdout.write(sys.argv[1].title())" $$app_name`; \
	mkdir -p ariane/apps/$$app_name; \
	envdir envs/$(ENV) python manage.py startapp $$app_name ariane/apps/$$app_name --template ariane/config/app_template; \
	echo "Don't forget to add 'ariane.apps."$$app_name".apps."$$app_name_title"Config' to INSTALLED_APPS in 'ariane.config/settings/common.py'!"

test:
	envdir envs/test python -m pytest $(TEST_ARGS) tests/

test-all: coverage-js
	tox

test-js:
	python -c "import os, webbrowser; webbrowser.open('file://{}/tests/jstests/index.html'.format(os.getcwd()))"

test-upload:
	twine upload -r test -s dist/*
	python -c "import webbrowser; webbrowser.open('https://testpypi.python.org/pypi/ariane')"

upload:
	twine upload -s dist/*
	python -c "import webbrowser; webbrowser.open('https://pypi.python.org/pypi/ariane')"
