#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import  sqlite3

dbdir = os.path.join(os.path.expanduser("~"),"desktop/moisework")
dbfile = os.path.join(dbdir,"moise.sqlite")

class essaiDB():
    def __init__(self):
        try:
            conn = sqlite3.connect('moiseLite.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS pilot_try(pilot_name1 TEXT,pilot_name2 TEXT, datetime_1 TEXT,datetime_2 TEXT )''')
            c.execute('''INSERT INTO pilot_try VALUES('marc morgand','jacques de beauregard','12/12/2000 10:00','12/12/2000 11:00')''')
            c.execute('''INSERT INTO pilot_try VALUES('francois morgand','antoine dupont','17/01/2001 11:30','12/01/2001 13:00')''')
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("ERREUR:  {}".format(e))





if __name__ == '__main__':
    essaiDB()







# def DatabaseUtility():
#     db = QSqlDatabase.addDatabase("QSQLITE")
#     db.setDatabaseName("moise.db")
#     db.open()
#
#
# def create_table(self):
#     query = QSqlQuery()
#     query.exec_("CREATE TABLE first_table (id INTEGER PRIMARY KEY UNIQUE NOT NULL ,pilot_1 CHAR NOT NULL, DATE_1 INT NOT NULL )")
#     query.exec_("INSERT INTO first_table (pilot_1,date_1)VALUES ('MARC','2012-12-12')")
#     QSqlQuery.lastError()
#
# if __name__ == '__main__':
#     DatabaseUtility()
