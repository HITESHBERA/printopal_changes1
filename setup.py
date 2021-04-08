# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in printopal_changes/__init__.py
from printopal_changes import __version__ as version

setup(
	name='printopal_changes',
	version=version,
	description='ERPNext Changes for Printopal',
	author='nomi-g',
	author_email='nomi9639@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
