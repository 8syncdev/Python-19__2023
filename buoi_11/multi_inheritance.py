'''
    class LớpCon(LớpCha1,LớpCha2,...)
    chuyên biệt hóa: 
        mỗi lớp là phục vụ cho 1 chức 
'''

class LopA:
    def __init__(self, name: str) -> None:
        self.name = name.title()

    def ham_a(self):
        print("a")

    def __str__(self) -> str:
        return f'{self.name}'

class LopB(LopA):
    def __init__(self, date: int, name:str) -> None:
        self.date = date
        super().__init__(name)


    def ham_b(self):
        print("B")

    def __str__(self) -> str:
        return f'{self.date}'

class LopC(LopB):
    def __init__(self, name: str, date: int) -> None:
        super().__init__(date, name)
    
    def __str__(self) -> str:
        self.ham_a()
        self.ham_b()
        return super().__str__()
    
'''
    Cha lớn nhât là super(): truyền vô đầu tiên
    Lớp cha còn lại là truy cập thông qua từ khóa self
'''

lop_c = LopC("Huyen", 23)
print(lop_c)