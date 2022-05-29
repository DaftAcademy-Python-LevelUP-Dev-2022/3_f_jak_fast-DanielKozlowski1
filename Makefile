MODULE = .
LIBS        = $(MODULE)
PYTHON      = poetry run python
PRECOMMIT   = poetry run pre-commit



.PHONY: clean fmt lint test init shell run-stack down-stack scrape


.git/hooks/pre-commit:
	@${PRECOMMIT} install
	@${PRECOMMIT} autoupdate
	@touch $@

pyproject.toml:
	@touch $@

poetry.lock: pyproject.toml
	@poetry env use "$(shell which python)"
	@poetry install
	@touch $@

init: poetry.lock .git/hooks/pre-commit

shell: poetry.lock
	@poetry shell

clean:
	@find . -type f -name "*.pyc" -delete
	@rm -f poetry.lock



lint: poetry.lock
	@${PYTHON} -m black ${LIBS}
	@${PYTHON} -m autoflake --in-place --recursive --remove-all-unused-imports --expand-star-imports ${LIBS}
	@${PYTHON} -m isort ${LIBS}
	@${PYTHON} -m mypy ${LIBS}
	@${PYTHON} -m bandit --configfile .bandit.yaml --recursive ${LIBS}

test: poetry.lock
	@${PYTHON} -m coverage run -m pytest tests

coverage: test
	@${PYTHON} -m coverage report
