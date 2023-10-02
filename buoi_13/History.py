
class History:

    def __init__(self, cccd: str, full_name: str, email: str, password: str) -> None:
        # User(full_name, email, password)
        self.cccd = cccd
        self.full_name = full_name
        self.email = email
        self.password = password
        # Tài khoản mặc định là chưa được chấp nhận
        # active: kích hoạt
        self.active = False

    
    def __str__(self) -> str:
        return f'{self.full_name}'