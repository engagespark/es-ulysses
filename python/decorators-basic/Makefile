.PHONY: all
all:
	echo "env — install requirements into a new virtualenv"
	echo "test — Run the tests"

clean:
	rm -r env

env:
	virtualenv env
	pip install --upgrade pip setuptools
	pip install -r requirements.txt
	@echo "\nInstalled dependencies into 'env/' virtualenv."

setup: env
	. env/bin/activate
	echo "You're good to go!"
	echo "You're good to go! Run 'make test' and have fun!"

.PHONY: test
test:
	py.test test.py
