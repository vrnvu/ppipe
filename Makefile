# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help lint test run

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------------HELP-----------------"
	@echo "To install dependenceis: make install"
	@echo "To run the project: make run"
	@echo "To test: make test"
	@echo "To lint with flake8: make lint"
	@echo "------------------------------------"

test:
	poetry run pytest
	
run:
	poetry run uvicorn ppipe.webservice.main:app --reload

lint:
	poetry run flake8 .
