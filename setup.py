#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Install script.
"""

from setuptools import setup, find_packages
import django_insecure

setup(
    name='django-insecure',
    version=django_insecure.__version__,
    packages=find_packages(),
    author='Bruno Clermont',
    author_email='patate@fastmail.cn',
    license='MIT',
    description=open('README.txt').read(),
    url='https://github.com/bclermont/django-insecure',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
