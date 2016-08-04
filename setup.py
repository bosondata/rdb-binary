#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='rdb',
    version='0.2.1',
    author='Jan-Erik Rediger',
    author_email='badboy@archlinux.us',
    url='https://github.com/badboy/rdb-rs',
    keywords='redis dumpdb',
    description='RDB parsing & dumping library and utility',
    py_modules=['rdb'],
    include_package_data=True,
    data_files=[
        ('/rdb-binary', ['rdb']),
    ],
    entry_points={
        'console_scripts': [
            'rdb = rdb:main',
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ]
)
