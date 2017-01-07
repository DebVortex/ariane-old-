#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from codecs import open

from setuptools import find_packages, setup

from ariane import __version__


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read(*paths):
    """Build a file path from *paths and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()


extras_require = {}

requires = [
    'asgiref==1.0.0',
    'channels==0.17.3',
    'daphne==0.15.0',
    'Django==1.10.5',
    'dj-database-url==0.4.2',
    'django-braces==1.10.0',
    'django-configurations==2.0',
    'django-crispy-forms==1.6.1',
    'django-grappelli==2.9.1',
    'django-model-utils==2.6',
    'envdir==0.7',
    'psycopg2==2.6.2',
    'pytz==2016.10',
    'wit==4.2.0',
    'wikipedia==1.4.0'
]

setup(
    name='ariane',
    version=__version__,
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
