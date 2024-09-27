# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:19:27 2024

@author: ACER
"""

s=0 
n = int(input("Nhap n: "))
while n < 0:
    n = int(input("Nhap lai n: "))
for i in range(0,n+1):
    s = s + (2*i + 1)/(2*i + 2)
print(round(s, 2))
