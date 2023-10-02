'''
    số thực: float() -> ép kiểu dữ liệu
    số phức: i-> phần ảo,
    chuỗi: str() -> ép kiểu dữ liệu
        + được đặt trong nháy đơn ('') hoặc là nháy kép ("")
    format string:
        + in theo sự sắp đặt (3 cách nhưng các bạn chỉ học kĩ cách cuối)
        + pattern ()
'''

# I. Số thực - Float()
# Nó khả tự động xác định kiểu dữ liệu

so_thuc = float(3) # chuyển đổi số nguyên sang số thực

# Lưu ý: float() chỉ chuyển đổi số hoặc chuyển đổi chuỗi số, không được ép chữ cái

# so_thuc_1 = float('a') # sai vì giá trị truyền là chữ cái


# II. Số phức:
# cú pháp: tên_biến = phần thực(float, int) + (float, int)j
# Ví du:

# so_phuc = 5 + 3j
# # phần thực: 5, phần ảo: 3
# print(type(so_phuc))

# III. Chuỗi kí tự - Str:
# nGuyen vAn mInh -> Nguyen Van Minh
'''
    + được đặt trong '' hoặc ""
'''

chuoi = 'Nguyen van minh'

# He said: "It's cold"

# he_said = 'He said: "It's cold"'

# Lưu ý: nháy kép có thể chứa nháy đơn (bặc buộc toàn bộ là nháy đơn), nháy đơn có thể chứa nháy kép (bặc buộc toàn bộ là nháy kép)


# nháy kép bọc nháy đơn
chuoi_1 = " helo 'world' " # in ra: hello 'world'
# nháy đơn bọc nháy kép
chuoi_2 = ' """""""""""" ' # in ra: """"""""""""

# dấu ''' ''' hoặc """ """ thì nó có thể chứa tất cả kí tự

# he_said = '''He said: "It's cold"'''

# print(he_said)


# In theo khuôn mẫu:
# Cách 1: nhận diện dữ liệu (thân quen với các bạn học trước C/C++) - Rất cũ 
'''
    Nhân dạng:
    %i : số nguyên tương ứng int trong python
    %f: số thực tương ứng float trong python
    %s: chuỗi tương ứng str trong python
    Cú pháp:
        print(' nhận_diện ' % (biến_1,biến_2, ...))
'''
# Ví du:
# a = 1 # số nguyên -> %i
# implicit:
# print("a = %i" % (a)) # in ra: a = 1

# b = 1.5 # số thực -> %f
# print("b = %f" % (b)) # in ra: b = 1.5

# c = 'Nguyen Van A' # chuỗi -> %s
# print("c = %s" % (c)) # in ra: c = Nguyen Van A

# In ra số đăng sau dấu phẩy:

# cú pháp: print(' %.(số_lượng_số_lấy_ra_sau_dấu_phẩy)f ' % (biến_1,biến_2, ...))

# Ví dụ:

# a = 1.5
# print("%.10f" % (a)) 
# # lấy 10 số sau dấu phẩy.
# Lấy từ trái -> phải sau dấu phẩy đủ 10 số thì dừng.

# b = 1.567878899
# print("%.2f" % (b)) # làm tròn thành 1.57.

# Truyền nhiều tham số:
# x = 3
# y = 4 
# z = 5 

# print("%i %i %i"%(x,y,z)) # in ra: 3 4 5

# thập phân là chấm. Ví du: 1.2, 3.4, 4.5, ...

# Cách 2: Sử hàm có sẵn trong python -  Format()
# Cú pháp: print("{}".format(biến_1, biến_2, ...))

# a = 1
# print("a = {}".format(a)) # in ra : a = 1
# nhiều biến:
# x = 3
# y = 4
# z = 5
# t = 10
# # # slicing string python
# # # print("{} {} {}".format(x,y,z)) # in ra: 3 4 5
#                               #0 1 2 3 -> vị trí
# print("{2} {0} {3} {1}".format(x,y,z,t)) # in ra:  
# trong lập trình vị trí đâu tiên là vị trí: 0
# Lưu ý: có bao nhiêu biến thì sẽ có bấy hoặc {} để truyền vào.

# in ra số sau dấu phẩy: {:.(số_lượng_số_sau_dấu_phẩy)f}
# b = 1.5
# print("{:.10f}".format(b)) # in ra: 1.5000000000


# Cách 3: f'String' - Format'String'
# cú pháp: print(f'{tên_biến}')
# a = 1
# b = 2

# print(f'{a} {b}') # in ra: 1 2

# áp dụng với ''''''

# print(f'''
#     a + b = {a+b}
# ''') # in ra: a + b = 3

# trong {được_tính_toán}

# {tên_biến:.(số_lượng_số_sau_dấu_phẩy)f}

# c = 1.5
# print(f'{c:.10f}') # in ra: 1.5000000000

# Print Pattern:
'''
    + Khi truyền nhiều biến thì mặc định giữa các biến là dấu cách -> sep
    + Mặc định sau mỗi print là xuống hàng -> end
'''

# Dùng sep:
# a = 1
# b = 2
# c = 3
# kí tự : \n -> xuống hàng
# sep (seperate : ngăn cách giữa nhiều biến): ' ' mình có thể sửa
# end (end line : kết thúc 1 hàng): mặc định '\n' (xuống hàng)
# print(a,b,c) #in ra: 1 2 3
# print(a,b,c, sep='-') #in ra: 1-2-3
# # end: khi kết câu lệnh print thì để lai ' '
# print(a,b,c) #in ra: 1-2
# print(a,b,c) #in ra: 1-2
# print(a,b,c) #in ra: 1-2

# In theo căn lề giữa, căn lề trên, dưới:
# Ví du: -------------Menu------------
# Cú pháp: {tên_biến:(loại_kí_phụ)(<:căn trái | >: căn phải | ^: căn giữa)(số_lượng_kí_tự)}

_menu = "Menu"

# mặc định nếu không truyền kí tự phụ thì nó là khoảng trắng

print(f'{_menu:^50}') # căn giữa 
print(f'{_menu:-<50}') # căn trái 
print(f'{_menu:->50}') # căn phải 


