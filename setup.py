#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

extras_require = {}

requires = [
    'asgiref==0.13.3',
    'channels==0.16.1',
    'daphne==0.14.2',
    'Django==1.9.7',
    'dj-database-url==0.4.1',
    'django-braces==1.9.0',
    'django-configurations==1.0',
    'django-crispy-forms==1.6.0',
    'django-grappelli==2.8.1',
    'django-model-utils==2.5',
    'envdir==0.7',
    'psycopg2==2.6.1',
    'pytz==2016.4',
    'wit==4.1.0'
]

setup(
    name='ariane',
    version='0.1.0',
    description='A short description of the project.',
    long_description=read(BASE_DIR, 'README.rst'),
    author='Max Brauer <max@max-brauer.de>',
    author_email='max@max-brauer.de',
    packages=find_packages(),
    include_package_data=True,
    scripts=['manage.py'],
    install_requires=requires,
    license='BSD',
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
)
