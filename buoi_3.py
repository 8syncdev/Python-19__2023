# If Else:
'''
    codition: điều kiện.
    else: luôn luôn nằm ở cuối, phủ định lại tất điều kiện trên, chỉ có duy nhất 1 hoi
    chỉ thực hiện điều đúng và bỏ qua tất cả các điều kiện còn lại
    If (condition):
        thực hiện đoạn code trong if
    else: phủ định condition trên
        thực hiện đoạn code trong else
'''
# n = 18
# if n >= 18:
#     print('Đủ 18')
# else: # n < 18
#     print('Không đủ 18')
'''

    if codition:
        # thực code trong if, nếu condition đúng -> True
    elif condition_1:
        # thực code trong elif, nếu condition_1 đúng và điều kiện trươc nó phải sai
    elif condition_2:
    elif condition_3:
    elif condition:
    elif condition:
    elif condition:
    else:
        làm điều kiện
    so sánh bằng: ==,
    so sánh >=,<=, >, <
    so sánh khác: != (dấu ! và = ghi liền)
'''
# Phép so sánh trả về kiểu bool(True, False)
# khi dùng so sánh bao giờ cũng có 2 dấu trở lên, trừ dấu >,<
# so sánh bằng ==:
# print(1 == 1) # True
# # so sánh khác nhau !=:
# print(1 != 1) # False

# n = 19

# if n == 18:
#     print(18)
# elif n == 18: # n != 18
#     print(19)
# elif n == 18:
#     print(18)
# elif n == 18:
#     print(18)
# elif n == 18:
#     print(18)
# else:
#     print(19)

# diem = int(input()) # ép kiểu str(string: chuỗi kí tự) -> int (số nguyên)

# and: cả hai điều kiện được nối bởi phép và (and) thì phải tất cả đều đúng thì mới trả về đúng

# if diem >= 8:
#     print("HSG")
# elif diem >= 5: # nếu elif được chạy thì tưc là if đã sai => diem < 8
#     print("HSK")
# else:
#     print("HSTB")

# If độc lập 

# n = 18

# if n == 18: 
#     print(18)
# if n == 18: 
#     print(18)
# if n == 18: 
#     print(18)

# if n == 18:
#     print(18)
# elif n == 18:
#     print(18)
# elif n == 18:
#     print(18)

# Có nhiều điều kiện phải thực hiện tất cả thì toàn bộ if
# Có nhiều điều kiện nhưng chỉ muốn 1 điều kiện xảy ra -> if - elif - else.

# If lồng nhau:
'''
    if điều_kiện_1:
        if điều_kiện_2:
            code xảy ra điều_kiện_12 đúng
        elif điều_kiền_3:
            code xảy ra điều_kiện_13 đúng.
    else: # phủ định của điều_kiện_1
       code xảy ra khi điều_kiện_1 sai 
'''


diem = int(input())

if diem >= 5:
    if diem < 8: # 5 <= diem < 8
        print("HSK")
    else: # diem >= 8
        print("HSG")
else: # diem < 5
    print("HSTB")



# cách 2: chặn từ lúc 8 điểm:


if diem >= 8: # nhánh lớn
    print("HSG")
else: # diem < 8 nhánh lớn
    if diem >= 5: # 5 <= diem < 8 nhánh con
        print("HSK")
    else: # diem < 5 nhánh con
        print("HSTB")











