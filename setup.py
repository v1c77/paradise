#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by vici on 01/08/2017
# use pyenv template
import codecs
import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

about = {}
with open(os.path.join(here, "core", "__version__.py")) as f:
    exec(f.read(), about)

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()


# if sys.version_info < (2, 7):
#     required.append('requests[security]')
#     required.append('ordereddict')

setup(
    name='pihomeiot',
    version=about['__version__'],
    description='A test to build my homeiot.',
    long_description=long_description,
    author='vic1',
    author_email='heyuhuade@gmail.com',
    url='https://github.com/woailuoli993/pi-homeiot',
    packages=[],
    entry_points={
        'console_scripts': ['pihomeiot=pihomeiot:cli'],
    },
    install_requires=open('requirements.txt').readlines(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
