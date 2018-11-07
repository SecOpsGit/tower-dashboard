#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the 'License'); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import os
import setuptools

from towerdashboard import version

root_dir = os.path.dirname(os.path.abspath(__file__))
readme = open(os.path.join(root_dir, 'README.md')).read()

setuptools.setup(
    name='towerdashboard',
    version=version.__version__,
    packages=setuptools.find_packages(),
    author='Tower QE Team',
    author_email='ansible-tower-qe@redhat.com',
    description='Tower QE Dashboard',
    long_description=readme,
    install_requires=[],
    url='https://github.com/Spredzy/tower-dashboard',
    license='Apache v2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
    ]
)
