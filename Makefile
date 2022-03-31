include .env
# ENV_VARS = $(shell sed -nr "s@^([A-Za-z_]+): (.+)@\1=\2@ p" env-vars-local.yaml)
ENV_VARS = $(shell cat .env)

env_setup:
	$(foreach v,$(ENV_VARS),$(eval export $(v)))

install_to_pkg:
	pip install build
	pip install twine

build_pkg:
	python3 -m build

upload_pkg:
	python3 -m twine upload --skip-existing dist/*

tests: env_setup
	python3 -m unittest discover -s ./tests -p "*_test.py"
	