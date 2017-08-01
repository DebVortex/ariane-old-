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
    'asgiref==1.1.2',
    'channels==1.1.6',
    'daphne==1.3.0',
    'Django==1.11.4',
    'dj-database-url==0.4.2',
    'django-allauth==0.32.0',
    'django-braces==1.11.0',
    'django-configurations==2.0',
    'django-crispy-forms==1.6.1',
    'django-grappelli==2.10.1',
    'django-model-utils==3.0.0',
    'envdir==0.7',
    'psycopg2==2.7.3',
    'pytz==2017.2',
    'wit==4.3.0',
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
