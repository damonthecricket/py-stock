
#!bin/bash



echo "Run unit tests."

python -m unittest  unit_tests.main

echo "Clean."

if [ "$1" == --pyc ]; then
	find . -name \*.pyc -delete
fi

find . -type d -name __pycache__ -exec rm -r {} \+

echo "End."