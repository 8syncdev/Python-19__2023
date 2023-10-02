from sqlite3 import *

from data_sql import DataTypeSQL
from typing import *


class SQLBase:

    # Khởi tạo đối tượng:
    # private: không cho đối tượng
    def __init__(self,
                 path: str | None = "",
                 ) -> None:
        self.path = path
        self.cursor = None  # giá trị None là chưa kết nối
        self.db = None

    def connect(self):
        with connect(self.path) as db:
            cursor = db.cursor()
            self.cursor = cursor
            self.db = db

    # CRUD: Create - Read - Update - Delete:

    def create(self,
               table_name: str,
               *attr
               ):
        if self.cursor is None:
            raise Error

        query = f'''
            CREATE TABLE IF NOT EXISTS {table_name} {attr};
        '''.replace('\'','')
        print(query)
        print(attr)

        try:
            self.cursor.execute(query)

        except Exception as e:
            print("Lỗi: ",str(e))

    # Chức năng xóa bảng ra khỏi DB:
    def drop(self,
             table_name: str,
             ):
        if self.cursor is None:
            raise Error
        query = f'''DROP TABLE {table_name}'''
        self.cursor.execute(query)

    def insert(self,
               table_name: str,
               col_names: List[str],
               values: List[str]
               ):
        if self.cursor is None:
            raise Error
        
        para = ','.join(["?" for _ in [col_names,]])
        col_names = ','.join(col_names)
        # print(type(col_names), type(values))


        query = f'''
                    INSERT INTO {table_name} ({col_names})
                    VALUES ({para});'''
        print(query)
        values = tuple(values)
        # print(values)
        self.cursor.execute(query, values)
        self.db.commit()



