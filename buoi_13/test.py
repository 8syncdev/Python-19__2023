# Testing: unitest, pytest

list_users = [
    {
        "cccd": "456465411111",
        "full_name":"Nguyen Van A",
        "email": "dsadjlk@jkld.com",
        "password":"123"
    },
    {
        "cccd": "116465411111",
        "full_name":"Nguyen Van C",
        "email": "dlk@jkld.com",
        "password":"123"
    },
    {
        "cccd": "336465411111",
        "full_name":"Nguyen Van B",
        "email": "djlk@jkld.com",
        "password":"123"
    },
    {
        "cccd": "336465411133",
        "full_name":"Nguyen Van E",
        "email": "djlk@jkld.com",
        "password":"123"
    },
    {
        "cccd": "336465411122",
        "full_name":"Nguyen Van F",
        "email": "djlk@jkld.com",
        "password":"123"
    },
]


# Test Cases:
from User import User
from Banking import Banking


banking = Banking()

for user in list_users:
    banking.dang_ki(user["cccd"], user["full_name"], user["email"], user["password"])


# assert Banking.list_users.__len__() == 2
# print(Banking.list_users.__len__() == 2)
# print(banking.__str__())


# unitest: test tự động hóa khác với test thủ công(manual test)

user = User(**list_users[0])
# print(user.user_info())

from Admin import Admin

info_admin = {
        "cccd": "1"*12,
        "full_name":"DEV PYTHON",
        "email": "dev@python.com",
        "password":"python_19"
    }

admin = Admin(**info_admin)
admin.active_for_users()
admin.display_all_users()
