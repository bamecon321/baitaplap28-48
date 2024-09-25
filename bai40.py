# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:08:34 2024

@author: ACER
"""
s = 0
n = int(input("Nhap vao so n: "))
while n < 0:
    n = int(input("Nhap lai vao so n: "))
for i in range(1,n+1):
    s = s + 1/(2*i)
print("Ket qua la: ", round(s,3))
    
 