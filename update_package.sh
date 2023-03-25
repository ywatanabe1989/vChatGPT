g#!/bin/bash

rm -rf build dist/* src/vChatGPT.egg-info
python3 setup.py sdist bdist_wheel
# twine upload -r testpypi dist/*
twine upload -r pypi dist/*
## EOF
