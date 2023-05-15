test:
	pytest

parallel_test:
	pytest -n 3

all_tests:
	pytest --workers 3

rerun:
	pytest --reruns 2