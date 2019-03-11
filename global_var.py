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


def save_dbs():
    print("Saving database configuration...")
    parser = ConfigParser()
    global dbConfPath
    global dbsDic
    for sectionName, sectionValue in dbsDic.items():
        parser.add_section(section=sectionName)
        for key, value in sectionValue.items():
            parser.set(section=sectionName, option=key, value=value)
    with open(dbConfPath, 'w') as fw:
        parser.write(fw)


dirname = os.path.split(os.path.realpath(__file__))[0].replace('\\', '/')
dbConfFile = '/config/db.conf'
dbConfPath = dirname + dbConfFile
dbsDic = config_dic()
