build_pkg:
	python3 -m build

upload_pkg:
	python3 -m twine upload --skip-existing dist/*