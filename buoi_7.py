'''
    Hàm: chức năng dùng tự định nghĩa , tái sử dụng.
    Cú pháp: def tên_hàm(tham_số_1, tham_số_2, ... | không có tham số)
    + phạm vi mà các biến tạo ra nằm trong hàm
    Gọi hàm: sau chữ return trả về 1 giá trị
    + Không có giá trị trả về (không có chữ return) : tên_hàm()
'''
# def (definition)

# hàm không tham số
# def hello():
#     print("hello")


# hàm có tham số, không có chữ return
# def tong(a, b):
#     print(a+b)

# tong(1,2) # tong(1,2) -> print(1+2)

# có return

# def tong(a,b):
#     return a+b

# tinh_tong = tong(1,2) # tong(1,2) -> int: 1+2
# #=> tinh_tong = 1+2=3
# print(tong(1,2), tinh_tong)

# return dừng code ngay lập tức:
# hàm dựng tại câu lệnh return và giá trị trả về là giá trị sau return
# def tong(a, b):
#     return a + b
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")
#     print("Hello")

# print(tong(1,2))

# Truyền tham số mặc định:
# def __PRINT__(chuoi_ki_tu="", sep = " ", end = "\n", layout="left", sl_ki_tu=100):
#     if layout == "left":
#         print(chuoi_ki_tu, sep=sep, end=end)
#     else:
#         if layout == "right":
#             print(f'{chuoi_ki_tu:>10}')
#         elif layout == "center":
#             print(f'{chuoi_ki_tu:^10}')
# __PRINT__(chuoi_ki_tu="Hello", layout="right")


# def tinh_tong(a=0, b=0):
#     return a + b
# # Khi không biết tên biến thì: ctrl + dấu cách
# print(tinh_tong())

# Auto decorator: tự chú thích dữ liệu rõ ràng cho ngươi dùng hàm biết
# Cú pháp: tên_biến:dư_liệu1|dữ_liệu_2|... 
# Lưu ý đây không phải là ép kiểu nó không ảnh giá trị truyền vào
# None: không có, không tồn tại
# so_tien:int|None # có ý nghĩa biến so_tien có kiểu dữ liệu là int hoặc None(=> không truyền tham số vào)

# def tinh_luong(luong_co_ban:int | None = 200000, so_ngay:int | None = 30) -> int:
#     return luong_co_ban * so_ngay
# #  -> int: là cho người dùng biết giá trị trả về mang dữ liệu gì.
# # Any: bất kì => kiểu dữ liệu nào cũng được
# print(tinh_luong())

### LIST 

### HÀM 1: Nhập 1 list số (int) trên cùng 1 hàng:

def nhap_tren_1_hang_int() -> list:
    # input + split + ép kiểu
    # Cách 1:
    # __nhap__ = input().split() # -> [str, str, str]
    # __nhap__ = [ int(item) for item in __nhap__ ]
    # return __nhap__
    return [ int(item) for item in input().split() ]



'''
    [ int(item) for item in input().split() ] (1)
    + python nó thấy có câu lệnh input() bên trong (1) ra lệnh cho hệ thống dừng lại chờ cho tới khi mà người dùng nhập vào thì mới chạy
'''

def list_so_le(danh_sach:list) -> list:
    return [ item for item in danh_sach if item % 2 == 1 ] # %: chia lấy phần dư

def list_so_chan(danh_sach:list)-> list:
    return [ item for item in danh_sach if item % 2 == 0 ] # %: chia lấy phần dư
    
# Kỹ thuật 2 con trỏ:

# _nhap_ = nhap_tren_1_hang_int()
# gia_tri_can_tim = 9
# kiem_tra = False
# for index in range(len(_nhap_) // 2 + 1): # nó chỉ chạy tới giữa list và stop - 1 => + 1
#     if _nhap_[index] == 9 or _nhap_[len(_nhap_) - 1 -index] == 9:
#         kiem_tra = True # nếu tìm thấy thì kiem_tra = True.
#         print("Tim thay")
#         break

# if not kiem_tra:
#     print("Khong tim thay")

# Kiem tra mang doi xung: i và len - 1 - i

danh_sach = nhap_tren_1_hang_int()
kiem_tra = False
for index in range(len(danh_sach) // 2 + 1):
    if danh_sach[index] != danh_sach[len(danh_sach) - 1 - index]:
        kiem_tra = True
        print("Sai")
        break

if kiem_tra == False: # kiem_tra vẫn là False nghĩa là không có phần tử nào khác nhau:
    print("Đúng")

# # Ctrl + click
# nhap_tren_1_hang_int()


