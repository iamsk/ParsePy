#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(
    name='ParsePy',
    description="python sdk for parse.com",
    version='0.2',
    author='pktck',
    author_email="parsepy@paulkastner.com",
    packages=find_packages(),
    install_requires=['setuptools'],
)
