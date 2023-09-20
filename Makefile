install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black script/*.py 

lint:
	ruff check --fix .

test:
	py.test --nbval ./jupyter/fortune500_analyze.ipynb &&\
	cd tests &&\
	python3 -m pytest -vv  test_*.py
		
all: install format lint test 