# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:16:39 2024

@author: ACER
"""

n = int(input("Nhap vao so N: "))
s=1
while n <= 0 or n % 2 == 0:
    n = int(input("Nhap vao so N: "))
    if n > 0:
        for i in range(1,n+1):
            s = s * i 
print(f"Tính S = 1 * 2 * 3 * ... *{n} = {s}")
    
    