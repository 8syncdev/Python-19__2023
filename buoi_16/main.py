from sqlite3 import *
import random


with connect('./data.db') as db:
    cursor = db.cursor()
    cccd = '424242'
    name = 'Nguyen Van D'
    password = 'gfdgdfg'
    cursor.execute(f'''
        INSERT INTO User (cccd, full_name, password)
        VALUES (:cccd, :name, :password);
        ''', {
                "cccd": cccd,
                "name": name,
                "password": password
            }
        )

# db = connect('./data.db')
# cursor = db.cursor()

# DROP TABLE
# cursor.execute("""DROP TABLE IF EXISTS users""")
# # CREATE TABLE
# cursor.execute(
# """CREATE TABLE IF NOT EXISTS Manager(
# id INTEGER PRIMARY KEY,
# name TEXT,
# phone TEXT,
# email TEXT unique,
# password TEXT
# )"""
# )
# db.commit()
