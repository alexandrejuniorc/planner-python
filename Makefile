# Description: Makefile for running the project
# Author: Alexandre Junior

dev/install:
	@pip3 install -r requirements.txt
dev/start:
	@python3 run.py
dev/test:
	@pytest -s -v $(file)
