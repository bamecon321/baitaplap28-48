# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:19:28 2024

@author: ACER
"""
import math
n = int(input("Nhap so nguyen duong N: "))
for i in range(1,n+1):
    can = math.sqrt(n)
if i == math.sqrt(n)**2:
    print("So chinh phuong la: ", can)
else:
    print("Khong phai la so chinh phuong")
