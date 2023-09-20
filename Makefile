install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	py.test --nbval ./jupyter/fortune500_analyze.ipynb &&\
	cd tests &&\
	python3 -m pytest -vv  test_*.py

format:	
	black script/*.py 

lint:
	ruff check --fix .
		
all: install lint test format