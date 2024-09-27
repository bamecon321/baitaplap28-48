# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:49:07 2024

@author: ACER

"""

a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
c = int(input("Nhao vao so c: "))
if a + b > c or b + c > a or a + c > b and (a > b > c > 0):
    print("Day la 1 tam giac")
    if a == b or b == c or c == a:
      print("Day la tam giac can")
    elif a == b == c:
      print("Day la tam giac deu")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
      print("Day la tam giac vuong")
else:
      print("Khong phai la tam giac")
    
