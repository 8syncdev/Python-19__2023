'''
    tập trung vào App Banking:
        - list user.
        - list history.
'''

from Banking import Banking
from User import User

# Admin không có role (quyền) nên mình cho kế thừa từ User
class Admin(User):
    token = 'kopkopkok4312432ok4po34'
    banking = Banking() # banking : list_users, list_history

    def __init__(self, cccd: str, full_name: str, email: str, password: str) -> None:
        super().__init__(cccd, full_name, email, password)
        self.role = 'admin'


    def active_for_users(self):
        dem = 0
        for user in Banking().list_users:
            user_format = f'STT:{dem} ,CCCD: {user.cccd}\nFull Name: {user.full_name}\nEmail: {user.email}\nPassword: {user.password}'
            print(f'| {user_format:^20} |')   
            dem+=1
        so_lua_chon = list(map(int, input('Nhập STT tương ứng để kích hoạt: ').split()))
        # so_lua_chon = [2,3]
        for item in so_lua_chon:
            Banking.list_users[item].active = True
        

        
    def display_all_users(self):
        dem = 0
        for user in Banking().list_users:
            user_format = f'STT:{dem} ,CCCD: {user.cccd}\nFull Name: {user.full_name}\nEmail: {user.email}\nPassword: {user.password}\nActive: {user.active}'
            print(f'| {user_format:^20} |')   
            dem+=1
            

