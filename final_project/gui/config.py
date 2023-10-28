'''Cửa sổ giao diện sử dụng class Window'''
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

_window = ttk.Window(
    title="Final Project",
    resizable=(False,False), # chiều cao x rộng bị cố định
    size=(400, 700),
    position=(1920-400,0),
    themename="vapor"
)


STYLE_WINDOW = {
    "title":"Final Project",
    "resizable":(False,False), # chiều cao x rộng bị cố định
    "size":(400, 700),
    "position":(1920-400,0),
    "themename":"vapor"
}

FONT_TTK = ('sans', 18)

'''API'''
DOMAIN_API = 'http://127.0.0.1:8000/'
API_SIGN_UP = f'{DOMAIN_API}get-info-user'
API_SIGN_IN = f'{DOMAIN_API}sign-in'


