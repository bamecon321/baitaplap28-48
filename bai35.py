# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:45:12 2024

@author: ACER
"""
n = int(input("Nhap so nguyen n: "))
s = 0
if n > 0:
    for i in range(1,n+1,1):
        s = s + i
    print(f"S = 1 + 2 + 3 + ... + {n} = {s}")
    
    
