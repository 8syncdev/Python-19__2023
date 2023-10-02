# Bài 13
'''
Bài 13. Đổi ngày sang năm, tuần, ngày
Cho trước N ngày, hãy đổi N thành số năm, số tuần và số ngày. Biết rằng một năm có 365 ngày.
Input Format
Số nguyên không âm N
Constraints
0<=N<=1000000
Output Format
In ra số năm, tuần, ngày tương ứng với N ngày
Sample Input 0
373


Sample Output 0
1 1 1

# '''
# N = int(input())

# nam = N // 365 # số năm

# N %= 365 # N = N % 365

# tuan = N // 7

# N %= 7 # N = N % 7

# ngay = N // 1

# print(nam,tuan,ngay)

# Bài 15:
'''
Bài 15. Mua nước
Fullhouse muốn nấu một món súp. Để làm điều đó, anh ta cần mua chính xác n lít nước. Chỉ có hai loại chai nước trong cửa hàng gần đó - chai 1 lít và chai 2 lít. Có vô số chai của hai loại này trong cửa hàng. Chai loại thứ nhất có gía a VNĐ và chai loại thứ hai có giá tương ứng b VNĐ. Fullhouse muốn chi càng ít tiền càng tốt. Nhiệm vụ của bạn là tìm ra số tiền tối thiểu (bằng VNĐ) fullhouse cần mua chính xác n lít nước ở cửa hàng gần đó nếu chai loại thứ nhất có giá a burles và chai loại thứ hai có giá b burles.
Input Format
3 số n,a,b là số nguyên (mỗi số 1 dòng)
Constraints
1<=n<=10^12; 1<=a,b<=1000
Output Format
Số tiền ít nhất để mua được n lit nước. Chú ý bạn phải mua chính xác n lít nước, không mua thiếu cũng không mua thừa.
Sample Input 0
10 1 3


Sample Output 0
10

'''

# Cách làm: đổi về cùng 1 cách đo là số lit

# n,a,b = int(input()), int(input()), int(input())

# if (2*a < b):
#     print(a*n)
# else:
#     if n % 2 == 1:
#         print(n*b/2 + (n % 2)*a)
#         '''
#             n*b/2: là chai 2lit của b VNĐ
#             n%2: sau khi em chai 2lit của b VNĐ còn dư thì mua tiếp chai a((n%2)*a)
#         '''
#     else:
#         print(n*b/2)

# Bài 19:
'''
Bài 19. Lát đá quảng trường
Quảng trường Nhà hát ở thủ đô Berland có hình chữ nhật với kích thước n × m mét. Nhân dịp kỷ niệm thành phố, một quyết định đã được đưa ra để lát Quảng trường bằng những viên bằng đá granit vuông. Mỗi viên đá hình vuông có kích thước a × a.
Số lượng viên đá ít nhất cần thiết để lát Quảng trường là bao nhiêu? Nó được phép che phủ bề mặt lớn hơn Quảng trường Nhà hát. Nó không được phép phá vỡ các viên đá. Các cạnh của viên đá phải song song với các cạnh của Quảng trường.
Gợi ý : Tính xem cần bao nhiêu viên đã để phủ kín chiều rộng, chiều dài của HCN rồi đem nhân vs nhau sẽ ra số viên đá cần, chú ý trường hợp n và m chia hết cho a hoặc ko chia hết.
Input Format
3 số nguyên dương n, m, a. (mỗi số 1 dòng)
Constraints
1<=n,m,a<=10^9
Output Format
Viết số lượng viên đá cần thiết để lát kín quảng trường.
Sample Input 0
6 
6 
4


Sample Output 0
4

'''

# n,m,a = int(input()), int(input()), int(input())


# if (n % a == 0): 
#     chieu_dai  = n // a 
# else: # n % a != 0
#     # khi nó dư gạch thì dùng 1 viên để lắp lại
#     chieu_dai= n // a + 1


# if (m % a == 0): 
#     chieu_rong = m // a 
# else: # m % a != 0
#     # khi nó dư gạch thì dùng 1 viên để lắp lại
#     chieu_rong = m // a + 1

# print(chieu_dai* chieu_rong)


# Bài 1. Tính toán giá trị của biểu thức

# n = int(input())
# print(pow(n,3) + pow(n, 2) + n +1)

# Bài 2. Tính toán giá trị biểu thức 2

# a,b,c = int(input()), int(input()), int(input())
# print( a*(b+c)+b*(a+c))

# Bài 3. Đổi nhiệt độ

# C = int(input())

# print((C * 9 / 5) + 32)


# Bài 4. Chu vi và diện tích hình tròn

# PI = 3.14
 
# R = int(input())
# print(f'{2 * PI * R:.4f} {PI * R * R:.4f}')

# Bài 5. Khoảng cách Euclid.
from math import *

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input()), 
# distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

# print(f'{distance:.2f}')

# Bài 6. Luyện tập viết câu điều kiện

# n = int(input())

# # && == and , || == or
# cau1 = "YES" if n % 2 == 0 else "NO" # no dung duoc trong elif
# cau2 = "YES" if n % 3 == 0 and n % 5 == 0 else "NO"
# cau3 = "YES" if n % 3 == 0 and n % 7 != 0 else "NO"
# cau4 = "YES" if n % 3 == 0 or n % 7 == 0 else "NO"
# cau5 = "YES" if n > 30 and n < 50 else "NO"
# cau6 = "YES" if (not n < 30) and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0) else "NO"
# cau7 = "YES" if n >= 10 and n <= 99 and (n % 10 == 2 or n % 10 == 3 or n % 10 == 5 or n % 10 == 7) else "NO"
# cau8 = "YES" if n <= 10 and n % 23 == 0 else "NO"
# cau9 = "YES" if not (n >= 10 and n <= 20) else "NO" # n < 10 or n > 20
# cau10 = "YES" if n % 10 % 3 == 0 else "NO"

# print(cau1,cau2, cau3,cau4,cau5, cau6 ,cau7, cau8, cau9, cau10, sep='\n')

# Bài 7. Số lớn nhất và nhỏ nhất
# a,b  = int(input()), int(input())

# print(f'{a // b * b}\n{(a + b - 1)// b * b}')

# Bài 9.Kiểm tra năm nhuận
'''
Năm nhuận là năm chia hết cho 400 hoặc (chia hết cho 4 và không chia hết cho 100). Nhập vào N là một năm và kiểm tra xem N có phải là năm nhuận hay không?
'''


# n = int(input())

# dap_an = "YES" if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0) else "NO"

# print(dap_an)


# a, b, c = int(input()), int(input()), int(input())

# dap_an = "YES" if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a else "NO" # kiem tam giac
# print(dap_an)

# Bài 11. Kiểm tra tam giác

# a, b, c = int(input()), int(input()), int(input())

# if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
#     if a == b and b == c:
#         print("1")
#     elif a == b or b == c or c == a:
#         print("2")
#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("3")
#     else:
#         print("4")
# else:
#     print("INVALID")

# Bài 12. Số ngày của tháng

# t, n = int(input()), int(input())

# if t >= 1 and t <= 12 and n >= 0:
#     if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
#         if t == 2:
#             print(29)
#         elif t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12:
#             print(31)
#         else:
#             print(30)
#     else: # nam khong nhuan
#         if t == 2:
#             print(28)
#         elif t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12:
#             print(31)
#         else:
#             print(30)
# else:
#     print("INVALID")

# Bài 14. Xếp loại học sinh

# d1,d2,d3,d4 = float(input()),float(input()),float(input()),float(input()),
# dtb = (d1+d2+2*d3+3*d4) / 7

# if dtb >= 8:
#     print("GIOI")
# elif dtb >= 6.5:
#     print("KHA")
# elif dtb >= 5:
#     print("TRUNG BINH")
# else:
#     print("YEU")

# Bài 16. Kí tự kế tiếp
# ket qua yeu cau la chu thuong
# chu_cai = input().lower() # lower: chu thuong

# if chu_cai == 'z':
#     print('a')
# else:
#     print(chr(ord(chu_cai)+1))

# Bài 17. Kiểm tra chữ cái

# chu_cai = input()

# if "A" <= chu_cai and  chu_cai <= "Z": # in hoa
#     print("UPPER")
# elif "a" <= chu_cai and chu_cai <= "z":
#     print("LOWER")
# elif "0" <= chu_cai and chu_cai <= "9":
#     print("DIGIT")
# else:
#     print("SPECIAL")


# Bài 18. Chuyển đổi in hoa in thường

# chu_cai = input()
# if "A" <= chu_cai and  chu_cai <= "Z": # in hoa
#     chu_cai = chu_cai.lower()
# elif "a" <= chu_cai and chu_cai <= "z":
#     chu_cai = chu_cai.upper()

# print(chu_cai)

# Bài 20. Frog

# a,b,k = int(input()), int(input()), int(input())

# if k % 2 == 0:
#     print(k // 2 * a - k // 2 * b)
# else:
#     print((k // 2 + 1) * a - k // 2 *b)


# Bài 21. Đồng xu


# n , s = int(input()), int(input())

# if s % n == 0:
#     print(s // n)
# else:
#     print(s // n + 1)

# Bài 22. Số lớn nhất nhỏ nhất trong 4 số

# a,b,c,d = int(input()),int(input()),int(input()),int(input()),

# print(max(a,b,c,d),min(a,b,c,d))


# round(): chi doi so float
# Bài 23. Làm tròn số

# n = float(input())

# # n = 15.5 - int(15.5)->15 = 0.5
# if (n - int(n) >= 0.5):
#     n = ceil(n)
# else:
#     n = floor(n)
# print(n)



