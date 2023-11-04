#!/bin/bash
# https://packaging.python.org/en/latest/tutorials/packaging-projects/

if [[ -d "./dist" ]];
then
    rm -r ./dist
fi

tox -r && \
python3 -m build && \
python3 -m twine upload --repository testpypi dist/*