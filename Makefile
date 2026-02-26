
package:
	python3 -m pip install --upgrade build
	python3 -m build
	ls -l dist

clean:
	rm dist/*

upload_test: package
	python -m pip install --upgrade twine
	python -m twine upload --repository testpypi dist/*

upload:	package
	python -m pip install --upgrade twine
	python -m twine upload dist/*

test_install:
	python -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple aes70py
