'''
    - Lưu ý:
        - Tất cả các chức năng (def: hàm, mỗi hàm là 1 chức năng) thì phải được xây dựng trong chương trình phụ
        - Hàm nào cần sử dụng thì gọi vào phần chương trình chính (if __name__ == '__main__':)
    - từ khóa pass là đưa vào tránh lỗi chứ không có chức năng gì hết.
    - Iterable (tập hợp): list, string, range
        + Sắp học: set, tuple, dictionary
    - Ứng dụng: học kĩ list, dict, set
    - OOP thời hiện đại thì đối tượng đơn giản dict 
'''
# Chủ đề: Quản lý nhà hàng
thoat_menu, xac_nhan_food, xac_nhan_water = '','',''
def menu():
    global thoat_menu, xac_nhan_food, xac_nhan_water
    '''
        - Menu:
            - Có danh sách các sự lựa chọn:
                + Danh sách món ăn (list)
                + Danh sách nước uống (list)
            - Chọn 1 phần tử từ danh sách trả 1 vị trí:
        - Pham vị của biến
    '''
    list_food = ['gà rán', 'bò', 'mì']
    list_water = ['soda','cam', 'chanh']
    lua_chon = input('Nhấn 0 để chọn thức ăn, nhấn 1 để chọn nước uống: ')
    
    if lua_chon == '0':
        for index in range(len(list_food)):
            print(f'{index+1}. {list_food[index]}')
        xac_nhan_food = input()
    elif lua_chon == '1':
        for index in range(len(list_water)):
            print(f'{index+1}. {list_water[index]}')
        xac_nhan_water = input()
    else:
        lua_chon = input('Nhập lại: ')
    thoat_menu = input('Nhấn 5 để thoát, nhấn bất phím khác 5 để chạy tiếp: ')

# Injection (DI): nâng cấp 1 nơi mà nhiều nơi cũng được nâng cấp theo.
def order():
    global thoat_menu, xac_nhan_food, xac_nhan_water
    if xac_nhan_food != '' and (xac_nhan_food >= '1' and xac_nhan_food <= '3'):
        xac_nhan_lai = input('Đồng ý đặt food nhấn 1, ngược lại nhấn 0: ')
        return xac_nhan_lai
    else:
        xac_nhan_lai = input('Đồng ý đặt water nhấn 1, ngược lại nhấn 0: ')
        return xac_nhan_lai

def bill():
    pass


so_nguyen = 10
def tang(): # phạm vi bên trong hàm là local varible => global(toàn cục)
    # trùng tên nhưng vẫn có khả năng khác ô nhớ
    # lý do: python hiểu là bạn muốn truy cập ra biến so_nguyen => += 
    # access: truy cập
    # so_nguyen += 1
    global so_nguyen
    so_nguyen = 1

if __name__ == '__main__':
    # chỗ sau dấu : là nơi bắt đầu chương trình chính.
    # tang()
    # print(so_nguyen)
    # Bắt đầu gọi hàm menu()
    # list_order_food = []
    # list_order_water = []
    # gia_tri_xac_nhan_food, gia_tri_xac_nhan_water = '',''
    # while True:
    #     menu()

    #     if thoat_menu == '5':
    #         break
    #     else:
    #         if xac_nhan_food != '':
    #             gia_tri_xac_nhan_food = order()
    #         else:
    #             gia_tri_xac_nhan_water = order()

    #     if gia_tri_xac_nhan_food == '1':
    #         list_order_food.append(xac_nhan_food)
    #         gia_tri_xac_nhan_food = ''
    #     elif gia_tri_xac_nhan_water == '1':
    #         list_order_water.append(xac_nhan_water)
    #         gia_tri_xac_nhan_water = ''

    # print(list_order_food)
    # print(list_order_water)

    # from tên_thư_viên import hàm
    # thư_viện: file bên trong file có hàm phục vụ chức năng 

    from MATH import binh_phuong

    print(binh_phuong(4))

    '''
        Cấu trúc dự án:
            - File chạy chương (if name main): main.py
            - Underscored: đặt cách nhau = dấu gạch dưới
            - Đặt có ý nghĩa
    '''


        