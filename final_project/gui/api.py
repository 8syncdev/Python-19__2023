import requests
from typing import *
'''Sign Up User'''

class API:
    def __init__(self,
                 url: str,
                 data: dict | None = {}
                 ) -> None:
        self.url = url
        self.data = data

    def sign_up(self):
        res = requests.post(
            url=self.url,
            data=self.data
        )

        return res.json()
    
    def sign_in(self):
        res = requests.post(
            url=self.url,
            data=self.data
        )

        return res.json()
