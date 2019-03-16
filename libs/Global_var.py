# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser
import pandas as pd


class GlobalVar:
    def __init__(self):
        self.dirname = os.path.split(os.path.realpath(__file__))[0].replace('\\', '/')
        self.dbConfFile = '/../config/db.conf'
        self.dbConfPath = self.dirname + self.dbConfFile
        self.dbsDic = self.config_dic()
        self.dbsTypes = ('mysql', 'postgresql')
        self.confKeys = ('host', 'port', 'user', 'password', 'name', 'type')
        self.tables_df = None

    def config_dic(self):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(self.dbConfPath)

        # get section, default to postgresql
        dbs_dic = {}
        sections = parser.sections()
        for section in sections:
            db = {}
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
                dbs_dic[section] = db
        return dbs_dic

    def refresh_conf(self):
        self.dbsDic = self.config_dic()

    def save_dbs(self):
        parser = ConfigParser()
        for sectionName, sectionValue in self.dbsDic.items():
            parser.add_section(section=sectionName)
            for key, value in sectionValue.items():
                parser.set(section=sectionName, option=key, value=value)
        with open(self.dbConfPath, 'w') as fw:
            parser.write(fw)

    def new_dbs(self, dbsName):
        default_conf = {'host': '127.0.0.1',
                        'port': '1234',
                        'user': 'default',
                        'password': '12345',
                        'name': 'default',
                        'type': 'mysql'
                        }
        self.dbsDic[dbsName] = default_conf
        self.save_dbs()
