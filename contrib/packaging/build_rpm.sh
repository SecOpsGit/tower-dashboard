#!/usr/bin/env bash
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

set -eux

PATH_TO_PROJ=${PATH_TO_PROJ:-.}
PROJ_NAME=${PROJ_NAME:-tower-dashboard}
OUTPUT_DIR=${OUTPUT_DIR:-/tmp}
DATE=$(date +%Y%m%d%H%M)
SHA=$(git rev-parse HEAD | cut -c1-8)

# Setup: Ensure we start with a clean environment from rpmbuild and mock
#        and copy the spec file over
#
rm -rf ${HOME}/rpmbuild && mock --clean
rpmdev-setuptree
cp ${PROJ_NAME}.spec ${HOME}/rpmbuild/SPECS/


# Build: Generate the tar ball build a source rpm only and build through mock
#
pushd ${PATH_TO_PROJ}
python setup.py sdist
cp -v dist/* ${HOME}/rpmbuild/SOURCES/
sed -i "s/VERS/${DATE}git${SHA}/g" ${HOME}/rpmbuild/SPECS/${PROJ_NAME}.spec
rpmbuild -bs ${HOME}/rpmbuild/SPECS/${PROJ_NAME}.spec
mock -r epel-7-x86_64 rebuild  --resultdir=${OUTPUT_DIR} ${HOME}/rpmbuild/SRPMS/${PROJ_NAME}*
popd
