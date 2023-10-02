#      0 1 2 3 4 5
# lst = [1,2,3,4,5,6]

# chèn ở vị trị bất kì thay hàm insert => start == stop
# stop - 1 => 2 - 1 = 1

# lst[1:1] = [100000] 

# print(lst)

# thay thế 1 1 list trong list cũ: 
# lst[1:4] = [100000]
# print(lst)


# lst = [6,5,7,1,2,3,5,1,2,5,1]

# Sử dụng vị trí: (Dễ nhất)
# input_index = int(input())
# for index in range(len(lst)):
#     if lst[index] == 1 and index == input_index:
#         print(index)

# Dùng hàm index():
'''
    Toán tử so sánh con: in -> kiểm tra xem 1 giá trị có phải là con của 1 tập hợp hay không
'''

# khoi_tao = lst.index(1) # phát hiện ra vị trí đầu tiên

# while 1 in lst[khoi_tao:]:
#     if lst[khoi_tao] == 1:
#         print(khoi_tao)
#     khoi_tao+=1
#     # Vượt ra khỏi danh sách chưa
#     if khoi_tao == len(lst):
#         break

'''
    trong danh sách có nhiều số thì sau tìm ra nhiều số in ra vi số cuối
'''

# List Comprehension

'''
    tên_biến = [ tên_biến_trả_về for tên_biến_trả_về in tập_hợp if điều_kiện_đúng(thì tên_biến_trả_về mới được thực thi) ]
'''
# l = [1,2,1, 3,4,1,5,6]
# gia_tri = int(input())
# dap_an = [ index for index in range(len(l)) if l[index] == gia_tri ]
# print(dap_an[len(dap_an)-1])

'''
    Khi mình chưa rõ về hàm thì sẽ dùng kĩ thuật list slicing, duyệt và tạo list và append nó vào,
'''

### String Built-in (Tứ khóa để tự học liên tục)

'''
    Những hàm có sẵn trong 1 dữ liệu.
'''

### Split(): giá trị trả về là 1 list[str,str,...]

# 1 2 3 4 -> [1,2,3,4]
# Cắt tất cả khoảng trắng thừa
# ds = input().split() # 1 2 3 -> ['1', '2', '3']
# ds = [ int(item) for item in ds ] # không cần điều kiện cho list comp
# # ['1', '2', '3'] -> [1,2,3]
# print(ds)

# Hello, World => split(",")

# chuoi = "Hello, World,Alex".split() # ["Hello"," World"]
# print(chuoi)

##

# "".strip() # bỏ đi khoảng trắng ở đầu và cuối.
# input() -> string
# n = input()
# new_string = n.strip()
# print(n)

# Title: Nguyen Van A

chuoi = 'nguyen van a'
new_chuoi = chuoi.title()
new_chuoi = chuoi.lower() # viết thường tất cả chữ
new_chuoi = chuoi.upper() # viết hoa tất cả chữ
new_chuoi = chuoi.capitalize() # viết hoa 1 chữ cái đầu
print(chuoi, new_chuoi)

'''
    tất cả hàm trong python đều là giá trị copy.
'''

# chuẩn hóa tên:
# #   nGuyen    VAn   MANh
# chuoi = "  nGuyen    VAn   MANh  ".split()
# ["nGuyen","VAn","MANh"]
# ' '.join(chuoi) -> nGuyen VAn MANh
# chuoi.title() 

chuoi = " ".join("  nGuyen    VAn   MANh  ".split()).title()
print(chuoi)


# Join != Split
'''
    kí_tự_chuỗi.join(list)
    kí_tự_chuỗi nó đóng vai trò là sep
    [1,2,3] -> '-'.join(list)
    "1-2-3"
'''
