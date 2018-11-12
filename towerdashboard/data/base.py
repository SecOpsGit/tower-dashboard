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


ANSIBLE_VERSIONS = [
    {'name': 'devel'},
    {'name': 'stable-2.7'},
    {'name': 'stable-2.6'},
    {'name': 'stable-2.5'},
    {'name': 'stable-2.4'},
    {'name': 'stable-2.3'},
]

OS_VERSIONS = [
    {'name': 'rhel-7.6-x86_64', 'desc': 'RHEL 7.6', 'family': 'RHEL'},
    {'name': 'rhel-7.5-x86_64', 'desc': 'RHEL 7.5', 'family': 'RHEL'},
    {'name': 'rhel-7.4-x86_64', 'desc': 'RHEL 7.4', 'family': 'RHEL'},
    {'name': 'centos-latest-x86_64', 'desc': 'CentOS Latest', 'family': 'RHEL'},  # noqa
    {'name': 'ol-7.5-x86_64', 'desc': 'Oracle Linux 7.5', 'family': 'RHEL'},
    {'name': 'ubuntu-16.04-x86_64', 'desc': 'Ubuntu 16.04', 'family': 'Ubuntu'},  # noqa
    {'name': 'ubuntu-14.04-x86_64', 'desc': 'Ubuntu 14.04', 'family': 'Ubuntu'},  # noqa
]

# Taken from: https://access.redhat.com/support/policy/updates/ansible-tower
#
TOWER_VERSIONS = [
    {'name': 'In Development', 'general_availability': None, 'end_of_full_support': None, 'end_of_maintenance_support': None, 'end_of_life': None},
    {'name': 'Release 3.3', 'general_availability': '2018-09-12', 'end_of_full_support': '2019-03-12', 'end_of_maintenance_support': '2019-09-12', 'end_of_life': '2020-03-12'},
    {'name': 'Release 3.2', 'general_availability': '2017-10-02', 'end_of_full_support': '2018-04-02', 'end_of_maintenance_support': '2018-10-02', 'end_of_life': '2019-04-02'},
]

TOWER_OS = [
    {'tower': 'In Development', 'os': 'rhel-7.6-x86_64'},
    {'tower': 'In Development', 'os': 'rhel-7.5-x86_64'},
    {'tower': 'In Development', 'os': 'rhel-7.4-x86_64'},
    {'tower': 'In Development', 'os': 'centos-latest-x86_64'},
    {'tower': 'In Development', 'os': 'ol-7.5-x86_64'},
    {'tower': 'In Development', 'os': 'ubuntu-16.04-x86_64'},

    {'tower': 'Release 3.3', 'os': 'rhel-7.6-x86_64'},
    {'tower': 'Release 3.3', 'os': 'rhel-7.5-x86_64'},
    {'tower': 'Release 3.3', 'os': 'rhel-7.4-x86_64'},
    {'tower': 'Release 3.3', 'os': 'centos-latest-x86_64'},
    {'tower': 'Release 3.3', 'os': 'ol-7.5-x86_64'},
    {'tower': 'Release 3.3', 'os': 'ubuntu-16.04-x86_64'},
    {'tower': 'Release 3.3', 'os': 'ubuntu-14.04-x86_64'},

    {'tower': 'Release 3.2', 'os': 'rhel-7.6-x86_64'},
    {'tower': 'Release 3.2', 'os': 'rhel-7.5-x86_64'},
    {'tower': 'Release 3.2', 'os': 'rhel-7.4-x86_64'},
    {'tower': 'Release 3.2', 'os': 'centos-latest-x86_64'},
    {'tower': 'Release 3.2', 'os': 'ol-7.5-x86_64'},
    {'tower': 'Release 3.2', 'os': 'ubuntu-16.04-x86_64'},
    {'tower': 'Release 3.2', 'os': 'ubuntu-14.04-x86_64'},
]

TOWER_ANSIBLE = [
    {'tower': 'In Development', 'ansible': 'stable-2.7'},
    {'tower': 'In Development', 'ansible': 'stable-2.6'},
    {'tower': 'In Development', 'ansible': 'stable-2.5'},
    {'tower': 'In Development', 'ansible': 'stable-2.4'},
    {'tower': 'In Development', 'ansible': 'stable-2.3'},

    {'tower': 'Release 3.3', 'ansible': 'stable-2.7'},
    {'tower': 'Release 3.3', 'ansible': 'stable-2.6'},
    {'tower': 'Release 3.3', 'ansible': 'stable-2.5'},
    {'tower': 'Release 3.3', 'ansible': 'stable-2.4'},
    {'tower': 'Release 3.3', 'ansible': 'stable-2.3'},

    {'tower': 'Release 3.2', 'ansible': 'stable-2.7'},
    {'tower': 'Release 3.2', 'ansible': 'stable-2.6'},
    {'tower': 'Release 3.2', 'ansible': 'stable-2.5'},
    {'tower': 'Release 3.2', 'ansible': 'stable-2.4'},
    {'tower': 'Release 3.2', 'ansible': 'stable-2.3'},
]


RESULTS = [
    {'release': 'release_3.3.2', 'os': 'rhel-7.6-x86_64', 'ansible': 'stable-2.7', 'status': 'SUCCESS', 'job_id': 12},
    {'release': 'release_3.3.2', 'os': 'rhel-7.5-x86_64', 'ansible': 'stable-2.6', 'status': 'SUCCESS', 'job_id': 13},
    {'release': 'release_3.3.2', 'os': 'rhel-7.4-x86_64', 'ansible': 'stable-2.5', 'status': 'SUCCESS', 'job_id': 16},
    {'release': 'release_3.2.9', 'os': 'rhel-7.6-x86_64', 'ansible': 'stable-2.7', 'status': 'SUCCESS', 'job_id': 19},
    {'release': 'release_3.2.9', 'os': 'rhel-7.5-x86_64', 'ansible': 'stable-2.7', 'status': 'SUCCESS', 'job_id': 20},
    {'release': 'release_3.2.9', 'os': 'rhel-7.4-x86_64', 'ansible': 'stable-2.7', 'status': 'SUCCESS', 'job_id': 24},
    {'release': 'release_3.2.9', 'os': 'centos-latest-x86_64', 'ansible': 'stable-2.7', 'status': 'FAILURE', 'job_id': 24},
]
