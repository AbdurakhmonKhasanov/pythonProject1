"""
1/07/2023
Theme: Python dasturlash tili (1-part)
Author: Abdurakhmon Khasanov
"""

# familya = 'Mengliyev'
# ism = 'Shaydulla'
# tugilgan_yil = 1981
# print(familya, ism , tugilgan_yil, end = ".")
# familya = input("familyangizni kiriting: ")
# ism = input ("ismingizni kiriting : ")
# tugilgan_yil = input("tugilgan yilingizni kiriting: ")
# print(familya, ism, tugilgan_yil, end = ".")
# familya = input("familyangizni kiriting: ")
# ism = input("ismingizni kiriting : ")
# tugilgan_yil = input("tugilgan yilingizni kiriting: ")
# print(familya, ism, tugilgan_yil, end = ".")
# butun_son = int(input("butun son kiriting : ") )
# haqiqiy_son = float (input("haqiqiy son kiriting : "))
# satr = str(input("star kiriting : "))
# print("Siz kiritgan butun son: ", butun_son)
# print("Siz kiritgan haqiqy son: ", haqiqiy_son)
# print("Siz kiritgan satr: ", satr)
# satr = input("satrni kiriting: ")
# print(satr)
# a = int(input("son kiriting:"))
# # absolyut_qiymat = abs(a)
# print("absolyut qiyamt: ", abs(a))
# import math
# x = float(input("x: "))
# y = math.acos(x)
# print('acos=',y)

""" 
5/07/2023 
Theme: Python Dasurlash tili (2-part)
Author: Abdurakhmon Khasanov
"""

#Jumalni rostlikka tekshirish
# a= int(input('a: '))
# print(bool(a%2==1))

# a = int (input('a: '))
# b = int (input('b: '))
# c = bool(a>2 and b<=3)
# print(c)

# a = int (input('a: '))
# b = int (input('b: '))
# c = int (input('c: '))
# result =bool(a<=b and b<=c)
# print (result)

# a = int (input('a: '))
# b = int (input('b: '))
# c = int (input('c: '))
# result = bool (a<b and b<c )
# print(result)

""" 
6/07/2023 
Theme: Python dasturlash turlari (3-part)
Author: Abdurakhmon Khasanov
"""

# a = int(input("a: "))
# b= int(input("b: "))
# bitta_toq = bool(a%2==1 or b%2==1)
# print(bitta_toq)

# a = int(input("a: "))
# b = int(input("b: "))
# c= int(input("c: "))
# hammasi_musbat = bool(a>0 and b>0 and c>0 )
# print(hammasi_musbat)

# a = int(input("a: "))
# b = int(input("b: "))
# c= int(input("c: "))
# bittasi_musbat = bool(a>0 and b<0 and c<0)or(a<0 and b>0 and c<0)or(a<0and b<0 and c>0)
# print(bittasi_musbat)

# a = kkint(input("a: "))
# b = bool (a>9 and a<100 and a%2==0)
# print('Berilgan juft son: ', b)
#
# a = int(input("a: "))
# b = bool(s>99 and a<1000 and )
""" 
7.07.2023 
Theme : Python Dasturlash tili (4-part) 
Author: Abdurakhmon Khasanov
"""
import math
a= int(input("a: "))
x = math.floor(a/100)
y = math.floor(a/10%10)
z = math.floor(a/10)
result = bool()