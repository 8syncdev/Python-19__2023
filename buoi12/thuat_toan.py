'''
    Đếm số lượng kí tự xuất hiện nhiều nhất
'''

chuoi = 'aaaaklko'
list_ = [1,2,2,1,1,3]
_dssp = [
    {
        "price":4213213,
        "name":"dsads"
    },
    {
        "price":3123,
        "name":"ewqes"
    },
    {
        "price":3123,
        "name":"ewqes"
    },
]

_lst = [ item.get('price') for item in _dssp ]
max_price = max(_lst, key=[].count)
print(max_price)

# xu_ly_sp = map(lambda item: item.get('price') == max_price, _dssp)
# print(list(xu_ly_sp))

