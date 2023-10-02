'''
    Class Banking:
    - liên kết với nhiều User
    - list[User] => class User

    DI: Dependency Injection

'''

from User import User
from History import History

class Banking:
    # Static Filed:
    list_users = [] # [User, User, ...] ,  User: class
    list_history = [] # [History,...]

    def __init__(self) -> None:
        self.user:User = None
        self.history:History = None

    def dang_ki(self, cccd, full_name, email, password):
        # cccd, full_name, email, password = input('CCCD: '), input('FULL Name'), input('Email'), input('Password')
        if cccd.__len__() == 12:
            self.user = User(cccd, full_name, email, password)
            self.history = History(cccd, full_name, email, password)
            # Lọc ra trong list users có user bị trùng
            fillter_users = list(filter(lambda user : user.cccd == cccd, Banking.list_users))
            if fillter_users == []:
                Banking.list_users.append(self.user)
            else:
                Banking.list_users.remove(fillter_users[0])
                Banking.list_users.append(self.user)



    def dang_nhap(self, cccd, password ):
        # cccd, password = input('CCCD: '), input('PASSWORD: ')
        try:
            # nếu code không lỗi sẽ chạy vào try
            tim_kiem = [ item for item in Banking.list_users if item.cccd == cccd and item.password == password ]
            return tim_kiem[0]
        except:
            # nếu try bị lỗi thì chạy vào except:
            return 'Bị lỗi đăng nhập'
        
    def __str__(self) -> str:
        filter_list_users = [ user.__str__() for user in Banking.list_users ]
        return filter_list_users
        
