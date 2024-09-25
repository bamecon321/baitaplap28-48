# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:31:00 2024

@author: ACER
"""

n = int(input("Nhap vao so N: "))
while n <= 0 :
    n = int(input("Nhap lai vao so N: "))
if n > 0:
    s = 0
    for i in range(1,n+1):
            s = s + 1/i
print(f"S(n) = 1 + 1/2 + 1/3 +....+1/{n} = {s} ")
    
    