#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2011-2023 German Aerospace Center (DLR) and others.
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0/
# This Source Code may also be made available under the following Secondary
# Licenses when the conditions for such availability set forth in the Eclipse
# Public License 2.0 are satisfied: GNU General Public License, version 2
# or later which is available at
# https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
# SPDX-License-Identifier: EPL-2.0 OR GPL-2.0-or-later

# @file    rebuildSchemata.py
# @author  Michael Behrisch
# @date    2011-07-11

from __future__ import absolute_import
from __future__ import print_function
import os
import subprocess

homeDir = os.environ.get("SUMO_HOME", os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
for exe in "activitygen dfrouter duarouter marouter jtrrouter netconvert netgenerate od2trips polyconvert sumo".split():
    exePath = os.path.join(homeDir, "bin", exe)
    subprocess.check_call([exePath, "--save-schema", os.path.join(homeDir, "data", "xsd", exe + "Configuration.xsd")])
subprocess.call([os.path.join(homeDir, "bin", "netedit"), "--attribute-help-output",
                 os.path.join(homeDir, "docs", "web", "docs", "Netedit", "attribute_help.md")])
