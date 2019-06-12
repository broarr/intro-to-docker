#!/usr/bin/env python3

import requests

payload = {'text': 'Hello World!'}

r = requests.get(
    'https://artii.herokuapp.com/make',
    params=payload)

print(r.text)

# import MySQLdb
#
# db = MySQLdb.connect(
#     host='maria',
#     user='root',
#     passwd='root')
#
# print(db)
