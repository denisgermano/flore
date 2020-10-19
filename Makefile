test:
	@pytest -s -vvv ./tests

check:
	@black -l 80 --check --include="flore"

format:
	@black -l 80 --include="flore"


.PHONY: tests format check
