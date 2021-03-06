#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
 * Copyright (C) 2017 Hendrik van Essen
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
"""

import MySQLdb

import os
import sys

# append root of the python code tree to sys.apth so that imports are working
#   alternative: add path to riotam_backend to the PYTHONPATH environment variable, but this includes one more step
#   which could be forget
CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT_DIR = os.path.normpath(os.path.join(CUR_DIR, os.pardir, os.pardir))
sys.path.append(PROJECT_ROOT_DIR)

from riotam_backend.config import config


class MyDatabase(object):

    _db_connection = None
    _db_cursor = None

    def __init__(self):
        self._db_connection = MySQLdb.connect(config.db_config["host"],
                                              config.db_config["user"],
                                              config.db_config["passwd"],
                                              config.db_config["db"])

        self._db_cursor = self._db_connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)

    def __del__(self):
        self._db_cursor.close()
        self._db_connection.close()

    def query(self, query, params=None):
        return self._db_cursor.execute(query, params)

    def fetchall(self):
        return self._db_cursor.fetchall()

    def commit(self):
        return self._db_connection.commit()
