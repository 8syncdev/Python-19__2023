'''
    Các lớp con kế thừa phải chung bản chất với lớp cha
    Ví dụ sai: xe máy kế thừa Động vật
'''


class DongVat:

    def __init__(self, name: str, weight: int, height: int) -> None:
        self.name = name
        self.weight = weight
        self.height = height


    def di_chuyen(self) -> None:
        print('Di chuyển cơ bản')


    def __str__(self) -> str:
        return f'{self.name}, {self.weight}, {self.height}'

# Lớp con: Con chó
'''
    class LớpCon(LớpCha)
'''
class ConCho(DongVat):

    def __init__(self, name: str, weight: int, height: int, sua: bool) -> None:
        super().__init__(name, weight, height)
        self.sua = sua

    def di_chuyen(self) -> None:
        super().di_chuyen()
        print("Chạy rất nhanh")


    def __str__(self) -> str:
        return super().__str__() + f' {self.sua}'


con_cho = ConCho('pipi', 34, 100, True)
con_cho.di_chuyen()

print(1)