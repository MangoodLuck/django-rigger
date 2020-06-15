#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from os import path as os_path
import os

this_directory = os_path.abspath(os_path.dirname(__file__))
URL = 'https://github.com/MangoodLuck/django-rigger.git'
NAME = 'django-rigger'
VERSION = '1.0.3'
DESCRIPTION = 'rigger is a django toolset that provides a daily common tools'
if os.path.exists('README.md'):
    with open('README.md', encoding='utf-8') as f:
        LONG_DESCRIPTION = f.read()
else:
    LONG_DESCRIPTION = DESCRIPTION
AUTHOR = 'Xiao Man'
AUTHOR_EMAIL = 'cloudbye@163.com'
LICENSE = 'MIT'
PLATFORMS = [
    'linux',
]

def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description

def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name=NAME,
    version=VERSION,
    description=(
        DESCRIPTION
    ),
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=find_packages(),
    platforms=PLATFORMS,
    url=URL,
    install_requires=read_requirements('requirements.txt'),
    python_requires=">=3.5",
)

