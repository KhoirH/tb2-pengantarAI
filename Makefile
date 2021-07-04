.ONESHELL:

.PHONY: clean install tests run all

clean:
	find source -type f -name '*.pyc' -delete
	find source -type f -name '*.log' -delete

install:
	virtualenv venv; \
	source venv/Scripts/activate; \
	pip install -r requirements.txt;

tests:
	source venv/Scripts/activate; \
	python manage.py test

run:
	source venv/Scripts/activate; \
	python manage.py run

all: clean install tests run