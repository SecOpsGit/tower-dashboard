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

import flask
import json
import requests

from flask import current_app
from towerdashboard import db
from towerdashboard.jenkins import jenkins


@jenkins.route('/ansible-versions', strict_slashes=False)
def ansible_versions():
    db_access = db.get_db()

    versions = db_access.execute('SELECT * FROM ansible_versions').fetchall()
    versions = db.format_fetchall(versions)

    return flask.Response(
        json.dumps(versions),
        status=200,
        content_type='application/json'
    )


@jenkins.route('/os-versions', strict_slashes=False)
def os_versions():
    db_access = db.get_db()

    versions = db_access.execute('SELECT * FROM os_versions').fetchall()
    versions = db.format_fetchall(versions)

    return flask.Response(
        json.dumps(versions),
        status=200,
        content_type='application/json'
    )


@jenkins.route('/tower-versions', strict_slashes=False)
def tower_versions():
    db_access = db.get_db()

    versions = db_access.execute('SELECT * FROM tower_versions').fetchall()
    versions = db.format_fetchall(versions)

    return flask.Response(
        json.dumps(versions),
        status=200,
        content_type='application/json'
    )


@jenkins.route('/results', strict_slashes=False, methods=['POST'])
def results():
    payload = flask.request.json

    tower_query = 'SELECT id FROM tower_versions WHERE version = "%s"' % payload['tower'].capitalize()[:11].replace('_', ' ')
    ansible_query = 'SELECT id FROM ansible_versions WHERE version = "%s"' % payload['ansible']
    os_query = 'SELECT id FROM os_versions WHERE version = "%s"' % payload['os']

    db_access = db.get_db()
    db_access.execute(
        'INSERT INTO results (tower_id, ansible_id, os_id, status, url) VALUES ((%s), (%s), (%s), "%s", "%s")' % (tower_query, ansible_query, os_query, payload['status'], payload['url'])
    )
    db_access.commit()

    return flask.Response(
      json.dumps({'Inserted': 'ok'}),
      status=201,
      content_type='application/json'
    )


@jenkins.route('/releases', strict_slashes=False)
def releases():
    db_access = db.get_db()

    versions_query = 'SELECT * FROM tower_versions'
    versions = db_access.execute(versions_query).fetchall()
    versions = db.format_fetchall(versions)

    results_query = 'SELECT tv.id, tv.version, av.version as "ansible", ov.version as "os", ov.description as "os_description", res.status, res.created_at as "res_created_at", res.url FROM tower_versions tv JOIN tower_os toos ON tv.id = toos.tower_id JOIN os_versions ov on toos.os_id = ov.id JOIN tower_ansible ta ON tv.id = ta.tower_id JOIN ansible_versions av ON av.id = ta.ansible_id LEFT JOIN results res ON (res.tower_id = tv.id AND res.os_id = ov.id AND res.ansible_id = av.id) ORDER BY tv.version, ov.id, av.id'
    results = db_access.execute(results_query).fetchall()
    results = db.format_fetchall(results)


    print(current_app.config.get('TOWERQA_URL'))
    print(current_app.config.get('GITHUB_TOKEN'))

    branches = requests.get(
        current_app.config.get('TOWERQA_URL'),
        headers={'Authorization': 'token %s' % current_app.config.get('GITHUB_TOKEN')}
    ).json()
    res = [branch['name'] for branch in branches]

    for version in versions:
        if 'devel' not in version['version'].lower():
            _version = version['version'].lower().replace(' ', '_')
            _res = [r for r in res if r.startswith(_version)]
            _res.sort()
            version['next_release'] = _res[-1]
            version['next_release'] = version['next_release'].replace('release_', '')

    return flask.render_template('jenkins/releases.html', versions=versions, results=results)
