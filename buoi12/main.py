
dap_an = ''

with open('buoi12/FILE/INPUT.txt',mode='r', encoding='utf-8') as file:
    for item in file.readlines():
        dap_an += item 
    


with open('buoi12/FILE/OUTPUT.txt', mode='a', encoding='utf-8') as file:
    file.write('''
    2

''')


'''
    / : dùng dấu này
    \ : ko dùng
    Xuống hang: \n
    Hàm read() -> str:
        - for duyệt qua từng kí tự
        - đọc từng kí tự

    Hàm readline(): -> str
        - đọc từng kí tự trong hàng đầu tiên
        - for : duyệt qua từng kí tự

    Hàm readlines():  -> list[str]
        - đọc từng hàng
        - list[str,str,...]
        - for: duyệt qua từng hàng 

    Append: thêm vào cuối => mode : a
'''