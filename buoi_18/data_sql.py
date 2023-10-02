


'''
    datatype sql: int, text, 
'''

class DataTypeSQL:


    def __init__(self,
                 col_name: str,
                 dtype: str | None = "TEXT",
                 constraint: str | None = "", # NOT NULL, UNIQUE
                 custom_field: str | None = "",
                 key: str | None = "",
                 ) -> None:
        self.attr_name = ' '.join([ item for item in [col_name, dtype,key, constraint, custom_field] if item != "" ])

    def __str__(self) -> str:
        return self.attr_name


