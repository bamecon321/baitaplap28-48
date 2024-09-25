# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:37:56 2024

@author: ACER
"""
n = int(input("Nhap so nguyen n: "))
while n <= 0 or n % 2 != 0:
    n=int(input("Nhap lai so nguyen n: "))
s = 0
if n > 0 and n % 2 == 0:
    for i in range(2,n+1,2):
        s = s + i
    print(f"S = 2 + 4 + 6 + ... + {n} = {s}")

