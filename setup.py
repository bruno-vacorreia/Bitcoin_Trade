#!/usr/bin/python3
from codecs import open
from setuptools import setup, find_packages

setup(
    name='bitcoin_trade',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=list(open('requirements.txt'))
)
