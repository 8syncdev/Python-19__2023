'''
    Dictionary (Từ điển): lưu cặp giá trị key:value
        - key: từ khóa chính để nhận dạng giá trị đó
        - value: giá trị của key
        Ví dụ: Học sinh có tên
        => dict(name:'Nguyen Van A')
        name chính key(khóa chính), 'Nguyen Van A' chính là value(giá trị)
        - có nhiều cặp
        Sinh viện: {
            name: 'Nguyen Van A',
            age: 20,
            height: 170,

        }
        Ví dụ: Sản phẩm nó sẽ có ngày sản xuất, giá_trị, độ bền, tên, model
        => key
        => {
            date: giá_trị,
            price: giá_trị,
            độ_bềnL giá_trị,
            tên: giá_trị,
            model: giá_trị,

        }
        l = [] # [
            {...},
            {...},
            {...},
        ]
        l.append({...})
        list() []
        dict() {}
'''
danh_sach_hs = [] # nhiệm vụ lưu lại nhiều dict (dict định nghĩa ra 1 học sinh)

n = int(input('Nhập bao nhiêu học sinh: '))
for item in range(n):
    hoc_sinh = {
        "ten": None,
        "tuoi": None,
        "ngay_sinh":None,
    }
    hoc_sinh["ten"], hoc_sinh["tuoi"], hoc_sinh["ngay_sinh"] = input(), input(), input()
    danh_sach_hs.append(hoc_sinh)

print(danh_sach_hs)

# hoc_sinh.get("ten")
# hoc_sinh["ten"] = input()

# print(hoc_sinh)





# hs = hoc_sinh
# print()