# List - List Slicing - List Comprehension

'''
    List: danh sách
    + Tập hợp lưu lại nhiều phần tử, các phần tử này có thể có dữ liệu khác,
    Cú pháp:
        + Kí hiệu: [] hoặc  list()
        tên_biến = []

    a = int(1) 
    a = list([])
    a = []
'''

# ds = []

# print(type(ds))

# Nhập tạo ra 1 list:

# n = int(input('n=')) # bởi input() -> str sau đó thì int(input()) : str -> int
# for i in range(n): # 0 -> n-1: n-1-0+1 = n | (số hang cuối(stop-1) - số hạng đầu(start))/step + 1
#     x = int(input('x='))
#     # hàm append để đưa 1 phần tử vào cuối danh sách
#     ds.append(x)
#     '''
#     Append:
#     Vòng lặp 1: x=1 -> [1]
#     Vòng lặp 2: x=2 -> [1,2]
#     Vòng lặp 3: x=3 -> [1,2,3]
#     '''
# print(ds)

# Ví du: 2,1,3,4
# 2 3 4 5 | split() của str


# Học các hàm các xử lý list
ds = []
# Count(đếm): đếm số lần xuất hiện của ds
ds = [1, 1, 1, 1, 2]
# print(ds.count(10))
# dem = 0
# tim_gia_tri = 10
# for item in ds:
#     if tim_gia_tri == item:
#         dem += 1
# print(dem)

# Index(vị trí, chỉ mục)
'''
    + Chỉ số bắt đầu trong danh sách là 0 kết thúc ở số_lượng_phần_tử-1
    + len(): lấy ra số lượng phần tư (int)
    Cú pháp: tên_ds[index]
'''

#     0  1  2  3  4  5
ds = [1, 1, 1, 5, 1, 2]
# print(len(ds)) # len = 6 thì mình phải chạy tơi len-1
# for index in range(0, len(ds)): # stop tự động - 1
#     # print(ds[index], end=' ')
#     ds[index] = 10
# # for item in ds:
# #     item = 1
# #     print(item, end=' ')

# print(ds)

# Lưu ý: for truy cập = index thì thay đổi được tập hợp

# ds = [1, 1, 1, 5, 1, 2]
# # Index(): in ra vị trí đầu tiên trong danh sách khi tìm thấy giá_trị(truyền vào)
# print(ds.index(1))

# Tìm vị tri của các giá trị giống nhau:

# ds.clear() # Xóa tất cả phần tử trong ds

# Chèn 1 giá trị vào trong danh sách:
'''
    Cú pháp: insert(vị_trí_cần_chèn, giá_trị_cần_chèn)
'''
#     0  1  2
ds = [1, 1, 1, 5, 1, 2]
# ds.insert(1, '100') # chèn chuỗi.
# ds.insert(1, 100) # chèn số.
# print(ds)

# Pop(vị_tí) và Remove(giá_trị: xóa phần tử.

# ds.pop() # mặc định là xóa ở cuối
# ds.pop(2) # ds.pop(vị_trí) nếu vị_trí không tồn tại thì gây ra lỗi.

# print(ds)

# ds.remove(5)
# ds.remove(1) # có nhiều số giống nhau chỉ xóa 1 sô đầu tiên
# print(ds)



# ds = [1, 1, 1, 5, 1, 2]
# l = ds.copy()
'''
    Sử dụng chung 1 giá trị
    Không được copy theo kiểu:
        a = 1
        b = a
    primitive type: str,int,float -> copy theo truyền thống
    preference type: list -> copy không theo kiểu truyền thống
'''

# l[0] = 1000
# print(ds)

# a = []
# b = []

# print(id(a), id(b))

# ds = [1, 1, 1, 5]

# # [1,2,3,1] + [1,2] = [1,2,3,1,1,2]

# ds.extend([1,2,3])
# print(ds)
# ds = [1, 1, 1, 5, 1, 2]
# ds.sort() # tăng dần <=> ds.sort(reverse=False)
# print(ds)
# ds.sort(reverse=True) # giãm dần
# print(ds)

# ds = [1, 1, 1, 5, 1, 2]
# ds_new = sorted(ds)
# ds_new = sorted(ds, reverse=True)
# print(ds_new, ds)

### List Slicing - Cắt Danh Sách
'''
    Cú pháp: ds_new = ds[start:stop:step] (start, stop -> là vị trí, step: bước nhảy)
    start: mặc định là chạy từ đầu vô(khi stop = 0) ,index = 0
    stop: vị trí cuối cùng, tự động trừ 1
    step: mặc định là 1
'''
#     0  1  2
ds = [1, 1, 1, 5, 1, 2]

# ds_new = ds[0:3] # start=0, stop=2
# print(ds[0:3])


# thay hàm copy
# ds_new = ds[:]
# print(ds_new)

# thay hàm insert
# thêm vào đầu:
ds[:0] = [1000]
# thêm vào cuối:
ds[len(ds)-1:]=[1000]
'''
    Cú pháp:
    ds[start:stop] = [giá_trị_cần_chèn]
'''
print(ds)






