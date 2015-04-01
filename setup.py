#!/usr/bin/env python

from setuptools import setup

setup(
    name='jsonschema-test',
    version='1.0.0',
    description='A tool for writing and running tests against a given JSON Schema.',
    url='https://github.com/kylef/jsonschema-test',
    packages=['jsonschema_test'],
    package_data={
        'jsonschema_test': ['schema.json'],
    },
    entry_points={
        'console_scripts': [
            'jsonschema-test = jsonschema_test:main',
        ]
    },
    install_requires=[
        'jsonschema',
    ],
    author='Kyle Fuller',
    author_email='kyle@fuller.li',
    license='BSD',
    classifiers=(
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'License :: OSI Approved :: BSD License',
    )
)

