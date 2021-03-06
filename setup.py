#!/usr/bin/env python

# Copyright 2017 Nicholas Bishop
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=missing-docstring

from setuptools import setup

setup(
    name='able',
    version='0.1.4',
    url='https://github.com/nicholasbishop/able',
    author='Nicholas Bishop',
    author_email='nicholasbishop@gmail.com',
    license='Apache 2.0',
    packages=['able'],
    install_requires=['TatSu~=4.2.3', 'lictionary~=0.1.2', 'six'],
    package_data={'able': ['grammar.ebnf']},
)
