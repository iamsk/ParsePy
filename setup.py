#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from setuptools import find_packages
from distutils.core import setup

setup(
    name='ParsePy',
    description="python sdk for parse.com",
    version='0.1',
    author='pktck',
    author_email="parsepy@paulkastner.com",
    packages=find_packages(),
    install_requires=['setuptools'],
)
