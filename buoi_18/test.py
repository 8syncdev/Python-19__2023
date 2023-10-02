


# def tong(*args):
#     print(args)



# tong(1,2,3,)


from base_sql import SQLBase, DataTypeSQL


id = DataTypeSQL(col_name="id", dtype="INTEGER", key="PRIMARY KEY", custom_field="AUTOINCREMENT")
name = DataTypeSQL(col_name="name", constraint="NOT NULL")

sql = SQLBase('./data.db')
sql.connect()
# sql.create("users",id.__str__(), name.__str__())
# sql.drop(table_name="users")

sql.insert(table_name="users", col_names=["name"], values=["Nguyễn Văn A"])