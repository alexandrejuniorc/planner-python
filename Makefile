# Description: Makefile for running the project
# Author: Alexandre Junior

dev/start:
	python3 run.py

dev/test:
	pytest -s -v $(file)
