#!/usr/bin/env python
# coding=utf-8

"""
安装文件
"""

import os
import sys

from setuptools import setup, find_packages
from pip.req import parse_requirements

from fdomain import VERSION


def get_reqs():
    install_reqs = parse_requirements('requirements.txt')
    return [str(ir.req) for ir in install_reqs]


setup(
    name='fdomain',
    version=VERSION,
    url='git@github.com:fooying/fdomain.git',
    description='Domain Format Library by Fooying',
    author='Fooying',
    author_email='f00y1n9@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    test_suite='nose.collector',
)

