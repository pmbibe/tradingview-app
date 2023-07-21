# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='tradingview-app',
    version='0.1.0',
    description='Screenshot Tradingview',
    long_description=readme,
    author='pmbibe',
    author_email='me@pmbibe.com',
    url='https://github.com/pmbibe/tradingview-app',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

