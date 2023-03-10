# Variables
PYTHON = python3
SRC_DIR = src

run_script:
	$(PYTHON) $(SRC_DIR)/main.py


clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	rm -f *.pyc
	rm -f .coverage
	rm -f coverage.xml
	rm -f junit.xml


