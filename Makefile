.PHONY: poetry-export test


poetry-export:
    poetry export --with dev --without-hashes -f requirements.txt -o requirements.txt

test:
    - coverage run -m pytest tests --junit-xml=".junit-report.xml"
	coverage report
