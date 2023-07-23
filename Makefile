PORT ?= 8000
install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

dev:
	poetry run flask --app page_analyzer:app run

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

