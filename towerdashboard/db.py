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

import datetime
import os
import sqlite3

from flask import current_app, g
from towerdashboard.data import base

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            SQLITE_PATH,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    if os.path.exists(SQLITE_PATH):
        return False

    with open('/tmp/init.sql', 'w') as f:
        print(str(base.ANSIBLE_VERSIONS))
        for version in base.ANSIBLE_VERSIONS:
            f.write(
                'INSERT INTO ansible_versions (version) VALUES ("%s");\n' % version['name']
            )

        for version in base.OS_VERSIONS:
            f.write(
                'INSERT INTO os_versions (version, description, family) VALUES ("%s", "%s", "%s");\n' % (version['name'], version['desc'], version['family'])
            )

        for version in base.TOWER_VERSIONS:
            f.write(
                'INSERT INTO tower_versions (version, general_availability, end_of_full_support, end_of_maintenance_support, end_of_life) VALUES ("%s", "%s", "%s", "%s", "%s");\n' % (version['name'], version['general_availability'], version['end_of_full_support'], version['end_of_maintenance_support'], version['end_of_life'])
            )

    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    with current_app.open_resource('/tmp/init.sql') as f:
        db.executescript(f.read().decode('utf8'))

    with open('/tmp/init.sql', 'w') as f:
        for config in base.TOWER_OS:
            tower_query = 'SELECT id FROM tower_versions WHERE version = "%s"' % config['tower']
            os_query = 'SELECT id FROM os_versions WHERE version = "%s"' % config['os']
            f.write(
                'INSERT INTO tower_os (tower_id, os_id) VALUES ((%s), (%s));\n' % (tower_query, os_query)
            )

        for config in base.TOWER_ANSIBLE:
            tower_query = 'SELECT id FROM tower_versions WHERE version = "%s"' % config['tower']
            ansible_query = 'SELECT id FROM ansible_versions WHERE version = "%s"' % config['ansible']
            f.write(
                'INSERT INTO tower_ansible (tower_id, ansible_id) VALUES ((%s), (%s));\n' % (tower_query, ansible_query)
            )

        for config in base.RESULTS:
            tower_query = 'SELECT id FROM tower_versions WHERE version = "%s"' % config['release'].capitalize().replace('_', ' ')[0:-2]
            os_query = 'SELECT id FROM os_versions WHERE version = "%s"' % config['os']
            ansible_query = 'SELECT id FROM ansible_versions WHERE version = "%s"' % config['ansible']
            f.write(
                    'INSERT INTO results (tower_id, ansible_id, os_id, status, url) VALUES ((%s), (%s), (%s), "%s", "%s");\n' % (tower_query, ansible_query, os_query, config['status'], 'https://www.google.com/')
            )

    with current_app.open_resource('/tmp/init.sql') as f:
        db.executescript(f.read().decode('utf8'))

    return True


def init_app(app):
    app.teardown_appcontext(close_db)


def format_fetchall(rows):

    _rows = [dict(row) for row in rows]
    for row in _rows:
        for key, value in row.iteritems():
            if type(row[key]) is datetime.datetime:
                row[key] = str(row[key])[:19]

    return _rows
