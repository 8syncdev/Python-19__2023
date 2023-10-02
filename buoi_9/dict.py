'''
    dictionary: <key:value>
    định nghĩa: dict(), {}
'''


# sinh_vien = {
#     "name": "Nguyen Van A",
#     "age": 25,
# }

# sinh_vien["age"] # 25
'''
    key: dạng str, int, float. Trong dict tạo => str
    Sử dụng dấu . để xem tất cả chức
'''
# sv2 = sinh_vien.copy()

# Constructor: dict() , {}

# sv2 = dict(sinh_vien)

# print({}.fromkeys(sinh_vien))
'''
    **{
    "name": "Nguyen Van A",
    "age": 25,
    }

    {
        "name": "Nguyen Van A",
        "age": 25,
    }
'''

# list_1 = [0,1,]
# list_2 = [ *list_1 ]


# print(id(sv2), id(sinh_vien))
# print((sv2), (sinh_vien))

'''
*args: Any => nhận vào list tham số [item1, item2 , item3, ...]
**kwargs: Any => nhận vào dict tham số là những cặp <key:value>
'''

'''
    items, keys, values: mục đích chung là lấy ra nhiều phần tử.
    items: lấy ra tất cả <key:value> -> dict[]
    keys: ->list[items_key,...]
    values: ->list(items_value)

    dùng trong trong trường hợp duyệt: for
'''


# for key, value in sinh_vien.items():
#     sinh_vien[key]

# for key in sinh_vien.keys():
#     print(key)


# sinh_vien = {}

# _key = input()

# sinh_vien[f'{_key}'] = input()
# print(sinh_vien)

'''
    List: khi mà muốn thay đổi truy cập thông qua vị trí,
    Dict: khi mà muốn thay đổi truy cập thông qua key,
    ví dụ:
        sinh_vien = {
            name: "Nguyen van A"
        }
        sinh_vien["name"] = ""
'''


# sinh_vien = {
#     "name": "Nguyen Van A",
#     "age" : 10,
# }

# new_info = {
#     "height": 170
# }

'''
    Bitwise: &, |, ^, ~,
    | : cộng, phép hợp 2 mã nhị phân
    0 | 1 = 1
    1 | 1 = 1
    0 | 0 = 0
'''

# sinh_vien |= new_info

# print(sinh_vien)
# print(bin(2)) # 0b010
# print(bin(5)) # 0b101

# print(5 | 2) #

