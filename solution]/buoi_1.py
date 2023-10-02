'''
Nhiệm vụ của bạn ở bài tập này rất đơn giản, bạn hãy nhập vào 1 số nguyên x và in ra 3 dòng : Dòng 1 là số x bạn vừa nhập từ bàn phím, Dòng 2 in ra dòng chữ "Hello World !" và dòng 3 in ra "fullhouse Python programming !"
'''

# n = int(input()) # ép kiểu
# Cách 1:
# print(n)
# print("Hello World !")
# print("fullhouse Python programming !")

#--------------
# Cách 2:
# sep: ngăn cách giữa các biến, mặc định là " "
# end: là kết thúc cuối câu, mặc định là "\n" (xuống hàng)
# print(n,"Hello World !", "fullhouse Python programming !",sep='\n')

#--------------
# Cách 3:
# print(f'''{n}
# Hello World !
# fullhouse Python programming !
# ''')

# Bài 2:
'''
Đề bài yêu cầu bạn nhập : Dòng 1 là số nguyên X, dòng 2 là số nguyên Y, dòng 3 là kí tự C, dòng 4 là số thực float F, dòng 5 là số thực float D. Nhiệm vụ của bạn là in ra 5 dòng. Dòng 1 in X, dòng 2 in Y, dòng 3 in C, dòng 4 in F với 2 số đằng sau dấu phẩy, dòng 5 in D với 9 số sau dấu phẩy.
Input Format
5 dòng lần lượt là X, Y, C, F, D
Constraints
-10^9<=X<=10^9; -10^18<=Y<=10^18; C là kí tự in hoa hoặc in thường; -10^6<=F<=10^6; -10^9<=D<=10^9;
Output Format
In ra 5 dòng theo yêu cầu
Sample Input 0
614
999999999999990528
G
19.088
2.9648


Sample Output 0
614
999999999999990528
G
19.09
2.964800000

'''

# x = int(input())
# y = int(input())
# c = input()
# f = float(input())
# d = float(input())

# print(f'''
# {x}
# {y}
# {c}
# {f:.2f}
# {d:.9f}
# ''')

# Bài 3:
'''
Cho 4 số X, Y, Z, T là số nguyên được nhập từ bàn phím. Bạn hãy in ra 3 dòng, dòng 1 lần lượt 4 số Y,Z,X,T mỗi số cách nhau một dấu phẩy, dòng 2 in ra tổng 4 số, dòng 3 in ra giá trị của biểu thử X - Y + Z * T. (Chú ý giá trị của tích Z * T và giá trị của tổng 4 số có thể tràn kiểu dữ liệu int)
Input Format
4 dòng chứa 4 số X, Y, Z, T
Constraints
1<=X, Y, Z, T <= 10^9
Output Format
In ra theo yêu cầu đầu bài
Sample Input 0
93 
9 
93 
98


Sample Output 0
9,93,93,98
293
9198

'''

# X,Y,Z,T = int(input()), int(input()), int(input()), int(input())
# print(f'''
# {X},{Y},{Z},{T}
# {X+Y+Z+T}
# {X - Y + Z * T}
# ''')

# Bài 4:
'''
Bài 4. Hàm pow
Cho 2 số x, y. Nhiệm vụ của bạn là tính x ^ y
Input Format
2 dòng chứa 2 số nguyên dương x, y 
Constraints
1<=x,y<=12;
Output Format
In ra x^y, nếu x^y có phần thập phân thì in ra 2 số sau dấu phẩy, nếu không có phần thập phân thì không cần in.
Sample Input 0
2 
2


Sample Output 0
4


Sample Input 1
4 
1


Sample Output 1
4

'''


# a ^ b: pow(a,b) = a ^b, a ** b

# a,b = int(input()), int(input())
# print(f'''
# {pow(a,b)}
# ''')

# n % m = x
'''
    module: mod = 10^9 + 7, a ^ b % mod = x => x <= mod
    5 % 2 = 1, khi n > m thì x <= m
    2 % 5 = 2, khi n < m thì x = n
'''

# Bài 5: Hàm sqrt và cbrt
'''
Cho số nguyên dương N, nhiệm vụ của bạn là tính căn bậc 2 và căn bậc 3 của N.
Input Format
Dòng duy nhất chứa số nguyên dương N
Constraints
1<=N<=10^9;
Output Format
Dòng 1 in ra căn bậc 2 của n với 2 số sau dấu phẩy; Dòng 2 in ra căn bậc 3 của n với 3 số sau dấu phẩy;
Sample Input 0
65


Sample Output 0
8.06
4.021


Sample Input 1
15


Sample Output 1
3.87
2.466

'''

# square root/ cube root python: sqrt(a)=> căn bậc hai của a, cbrt(a)=> căn bậc ba của a.
# Nằm trong thư viện toán học của python:
# from math import *

# n = int(input())
# print(f'''
# {sqrt(n):.2f}
# {cbrt(n):.3f}
# ''')

# ctrl + c: thoát
