# coding: utf8
""" 
@ File: data_clean.py
@ Editor: PyCharm
@ Author: Ace (From Chengdu.China)
@ HomePage: https://github.com/AceProfessional
@ OS: Windows 11 Professional Workstation 22H2
@ CreatedTime: 2023-04-08
"""

import sys

sys.dont_write_bytecode = True

from public.MySQLConnectionTools import MySQLConnection
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

sql = MySQLConnection(
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

count = 400

def movies_directors():
    pass

