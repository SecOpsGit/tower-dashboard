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
import os

from towerdashboard import db
from towerdashboard.jenkins import jenkins


def create_app():
    app = flask.Flask(__name__)
    if os.environ.get('TOWERDASHBOARD_SETTINGS'):
        app.config.from_envvar('TOWERDASHBOARD_SETTINGS')
    if not app.config.get('GITHUB_TOKEN'):
        raise RuntimeError('GITHUB_TOKEN setting must be specified')
    if not app.config.get('TOWERQA_URL'):
        raise RuntimeError('TOWERQA_URL setting must be specified')

    app.register_blueprint(jenkins)
    db.init_app(app)

    return app


app = create_app()


@app.route('/', strict_slashes=False)
def index():
    return flask.Response(
        json.dumps({'_status': 'OK', 'message': 'Tower Dasbhoard: OK'}),
        status=200,
        content_type='application/json'
    )


@app.route('/init-db', strict_slashes=False)
def init_db():
    if db.init_db():
        msg = 'Database initialized'
    else:
        msg = 'Database alaready initialized'

    return flask.Response(
        json.dumps({'_status': 'OK', 'message': msg}),
        status=200,
        content_type='application/json'
    )
