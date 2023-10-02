'''
    - Class User:
        - Dữ liệu cần thiết : cccd, full_name, email, password
        - Dữ liệu không cần thiết: nick_name
    - Bắc buộc:
        - Dữ liệu:
            - cccd: đúng 12 chữ số, full_name, email, password != ""
        - Đăng Kí:
            - user không có active
            - Dù dư liệu thành công, thất bại cũng phải lưu => không lưu trung 1 người bị sai quá nhiều.

'''
class User:

    def __init__(self, cccd: str, full_name: str, email: str, password: str) -> None:
        # User(full_name, email, password)
        self.cccd = cccd
        self.full_name = full_name
        self.email = email
        self.password = password
        # Tài khoản mặc định là chưa được chấp nhận
        # active: kích hoạt tài khoản
        self.active = False
        # quyền : user là admin hay là user
        self.role = 'user'

    def user_info(self):
        if self.active == True or self.role == 'admin':
            return f'CCCD: {self.cccd}\nFull Name: {self.full_name}\nEmail: {self.email}\nPassword: {self.password}'
        return 'Không được xem'
    
    def __str__(self) -> str:
        return f'{self.full_name}'
    

    