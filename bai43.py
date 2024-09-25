# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:13:48 2024

@author: ACER
"""

n = int(input("Nhap vao n: "))
s = 0
while n < 0:
    n = int(input("Nhap lai vao n: "))
for i in range(1,n+1):
    s += i/(i+1)
print("Ket qua la: ", round(s,3))