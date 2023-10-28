from config import _window, FONT_TTK, API_SIGN_UP
from api import API
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class Mainapp:

    def __init__(self) -> None:
        self._window = _window


        self._window.mainloop()