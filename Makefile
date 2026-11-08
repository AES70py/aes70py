
package:
	python3 -mvenv testvenv
	. testvenv/bin/activate && \
        python3 -m pip install --upgrade hatchling && \
        hatchling build && \
        rm -rf testenv
	ls -l dist

clean:
	-rm dist/*

verify: clean test package

# Run all tests with pytest
test:
	python3 -mvenv testvenv
	. testvenv/bin/activate && \
        pip install pytest && \
        pip install . && \
	python3 -mpytest tests/ -v && \
        rm -rf testenv
	# Alternative: python3 -m pytest tests/ --cov=src/aes70

upload_test: package
	python -m pip install --upgrade twine
	python -m twine upload --repository testpypi dist/*

upload:	package
	python3 -m pip install --upgrade twine
	python -m twine upload dist/*

test_install:
	python -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple aes70py
