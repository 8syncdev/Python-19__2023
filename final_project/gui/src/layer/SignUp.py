from config import _window, FONT_TTK, API_SIGN_UP, API_SIGN_IN, STYLE_WINDOW
from api import API
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.layer.MainApp import Mainapp
'''
    int => IntVar
    float => FloatVar
    str => StringVar
'''


class SignUp():

    def __init__(self) -> None:
        self.window = ttk.Window(**STYLE_WINDOW)
        self.window.configure(pady=50)
        self.style = ttk.Style()
        self.style.configure('TButton', font=FONT_TTK)

        self.username: ttk.StringVar = ttk.StringVar(value='', name='username')
        self.password: ttk.StringVar = ttk.StringVar(value='', name='password')
        '''Tạo giao diện'''
        self.create_input()
        self.create_btn()
        self.window.mainloop()

    def create_input(self):
        label_username = ttk.Label(text="Username: ", font=FONT_TTK)
        label_username.pack(fill=X, padx=20)
        #
        input_username = ttk.Entry(textvariable=self.username, font=FONT_TTK)
        input_username.pack(fill=X, padx=20)
        #
        label_username = ttk.Label(text="Password: ", font=FONT_TTK)
        label_username.pack(fill=X, padx=20)
        #
        input_username = ttk.Entry(textvariable=self.password, font=FONT_TTK)
        input_username.pack(fill=X, padx=20)

    def create_btn(self):
        btn_sign_up = ttk.Button(text="Đăng Kí", command=self.action_sign_up, style='TButton')
        btn_sign_up.pack(pady=20)
        btn_sign_up = ttk.Button(text="Đăng Nhập", command=self.action_sign_in, style='TButton')
        btn_sign_up.pack(pady=20)

    def action_sign_up(self):
        data = {
            'username': self.username.get(),
            'password': self.password.get()
        }

        api = API(url=API_SIGN_UP, data=data)
        print(api.sign_up())

    def action_sign_in(self):
        data = {
            'username': self.username.get(),
            'password': self.password.get()
        }

        api = API(url=API_SIGN_IN, data=data)
        res = api.sign_in()
        if res.get('detail') == 'success':
            print(res.get('detail'))
            self.window.quit()
            main_app = ttk.Window(**STYLE_WINDOW)
            main_app.mainloop()

        else:
            print(res.get('detail'))

