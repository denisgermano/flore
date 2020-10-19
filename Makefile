test:
	@pytest -s -vvv ./tests

check:
	@black -l 80 ./flore --check

format:
	@black -l 80 ./flore


.PHONY: tests format check
