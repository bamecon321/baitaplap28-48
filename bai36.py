# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:57:53 2024

@author: ACER
"""

n = int(input("Nhap so nguyen N: "))
s = 0
if n > 0:
    for i in range(1,n+1):
        s = s + i**2
print(f"Tính S = 1**2 + 2**2 + 3**2 + ... + {n**2} = {s}")

        