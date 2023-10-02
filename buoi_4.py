### RANGE(): sinh ra một tập hợp. Ví du: {1,2,3,4,5}
'''
    Cú pháp: range(start,stop,step)
    start: nếu không có thì chỉ số này mặc định là 0.
    stop: bặc buộc, chỉ chạy tới stop - 1. Ví dụ: range(5) -> 0,1,2,3,4
    step: bước nhảy hay khoảng cách giữa các số là bao nhiêu đơn. Ví dụ: range(0,5,2) -> 0,2,4
    thứ tự truyền là start->stop->step
    range(start,stop). Ví dụ: range(0,5)
'''

# Xem cái range(): list(range(5)) -> chuyển range thành danh sách, danh sách được trong [1,2,3,4]

# print(list(range(0,5,2)))


# Không có chỉ số bắt đầu (start), không có step = 1; start mặc định = 0
# print(list(range(10))) # chạy từ 0 -> 9 , stop - 1


# Sinh ra một dãy sô giãm dần 
'''
    Cú pháp: range(start,stop,step)
    start: nếu không có thì chỉ số này mặc định là 0.
    stop: bặc buộc, chỉ chạy tới stop + 1. 
    step: bước nhảy hay khoảng cách giữa các số là bao nhiêu đơn. 
    thứ tự truyền là start->stop->step
    range(start,stop). 
    Lưu ý: Start > Stop
'''
# print(list(range(5,2, -1)))

### For: duyệt qua từng phần tử trong tập hợp (range)
'''
    Cú pháp: for tên_biến_duyệt_qua_từng_giá_trị in tập_hợp(range)
    tên_biến_duyệt_qua_từng_giá_trị: tùy ý đặt tên nhưng phải có ý nghĩa. Thường đặt item (dịch ra; phần tử)
    tập_hợp(range): range sinh ra dãy số.
'''

# Print: măc định end = '\n'(xuống hàng), sep: mặc định là ' '
# for item in range(10):
#     print(item) 

'''
    range(10): 0 -> 9 (stop-1, start mặc định = 0)
    [0,1,2,3,4,5,6,7,8,9]
    Lần lặp 1: item = 0 -> print(0)
    Lần lặp 2: item = 1 -> print(1)
    ...
    Lần lặp 10: item = 9 -> print(9)
'''

'''
    Câu hỏi: khi mình thay đổi item trong for thì range có thay đổi hay không:
    Code ví dụ:
    day_so = range(10) # 0 -> 9
    for item in day_so:
        item = 1
    ??? day_so tất cả phần tử có = 1 không
    A. Có   B. Không
'''

# day_so = range(10) # 0 -> 9
# print(id(day_so)) # trước khi item = 1
# for item in day_so:
#     item = 1
#     print(item)
# '''
#     item = 0 -> item = 1 -> print(1) | range()
# '''

# print(id(day_so)) # sau khi item = 1

# Danh sách (list) kết hợp range: nó phải kiểu primitive type (int, float, str)


### Bảng cửu chương:

# n = int(input()) # input->str -> int (int(input())) : ép kiểu.

# for item in range(1,11):
#     print(f'|{n} x {item} = {n * item}|')

'''
|5 x 1 = 5|
|5 x 2 = 10|
|5 x 3 = 15|
|5 x 4 = 20|
|5 x 5 = 25|
|5 x 6 = 30|
|5 x 7 = 35|
|5 x 8 = 40|
|5 x 9 = 45|
|5 x 10 = 50|
'''

# n=int(input())
# _menu = "Menu"
# print(f'{_menu:-^16}')
# for item in range(1,11):
#     print(f'| {n:2d} x {item:2d} = {n * item:2d} |')


# {tên_biến:(số_khoảng_trắng_cho_trước)d}


# n = int(input())
# for item in range(1,10):
#     print(f'|{n} x {item} = {n * item:<2}|')

# n = int(input())

# for item in range(1,10):
#     bieu_thuc = f'{n} x {item} = {n * item}'
#     print(f'| {bieu_thuc:<11}| ')

# value = int(input())
# size = len('| '+str(value)+' x 10 = '+str(value*10)+' |')

# for item in range(1,11):
#     # print('|{} x {} = {}'.format(value,item,value*item))
#     size2 = len('| '+str(value)+' x '+str(item)+' = '+str(value*item)+' |')
#     if size==size2:
#         print('| '+str(value)+' x '+str(item)+' = '+str(value*item)+' |')
#     else:
#         print('| '+str(value)+' x '+str(item)+' = '+str(value*item)+' '*(size-size2)+' |')

### While: vòng lặp có điều kiện.
'''
    giá_trị_bắt_đầu = giá_trị
    while điều_kiện_dừng:
        # thực thi code khi điều kiện đúng
        bộ_đếm
'''

# gia_tri_bat_dau = 0

# while gia_tri_bat_dau < 5:
#     print(gia_tri_bat_dau)
#     gia_tri_bat_dau += 1 # gia_tri_bat_dau = gia_tri_bat_dau + 1


'''
    Lần lặp 1: 0 < 5 -> in ra 0 -> gia_tri_bat_dau += 1 (0-> 1)
    Lần lặp 2: 1 < 5 -> in ra 1 -> gia_tri_bat_dau += 1 (1 -> 2)
    ...
    Lần lặp 5: 4 < 5
'''

### Trước khi kết thúc vong lặp tôi làm 1 cái gì đó else trong for và while


for item in range(10):
    print(item)
else: # sau kết thúc vòng thì nó đi vào cái else nó làm tiếp công việc
    print('vong da ket thuc')
# else luôn luôn được thực thi sau khi for hết

item = 0

while item < 10:
    print(item)
    item += 1
else:
    print('while da ket thuc')