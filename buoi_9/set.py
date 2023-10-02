'''
    Set(), {} : Tập hợp
    set truyền 1 giá trị
    luôn được sắp xếp
    các phần tử không trùn nhau
    không có vị trí như list (unorder)
    => không truy cập thông thường
'''

# se = set()
# se.add(2)
# se.add(1) 
# se.add(1) 
# se = list(se)
# frozenset()
'''
    immutable: không thể thay đổi được
    Set: 
'''
# lambda:
'''
    tên_hàm = lambda tham_số1, tham_số2, ... : giá_trị_trả_về
    tên_hàm()
'''

chia_het_2 = lambda x : x % 2 == 0

# print(chia_het_2(3))

def chia_2(x):
    return x % 2 == 0

# map()

# ket_qua = list(map(chia_het_2, [1,2,3,5])) # lấy hết
ket_qua = list(filter(lambda x : x % 2 == 0, [1,2,3,5])) # lấy đáp án chính xác bỏ đáp án sai
print(ket_qua)