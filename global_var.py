# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser


def config_dic():
    global dbConfPath
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(dbConfPath)

    # get section, default to postgresql
    dbsDic = {}
    db = {}
    sections = parser.sections()
    for section in sections:
        db = {}
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
            dbsDic[section] = db
    return dbsDic


dirname = os.path.split(os.path.realpath(__file__))[0].replace('\\', '/')
dbConfFile = '/config/db.conf'
dbConfPath = dirname + dbConfFile
dbsDic = config_dic()
