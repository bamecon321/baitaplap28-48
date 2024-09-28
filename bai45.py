# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:55:33 2024

@author: ACER
"""

tu_so = 1
mau_so = 0
s=0
n = int(input("Nhap n: "))
while n <= 0:
    n = int(input("Nhap lai n: "))
x = float(input("Nhap x: "))
    for i in range(1,n+1):
        tu_so = n**i
        mau_so = mau_so + i
        s = s + tu_so / mau_so
print(round(s, 2))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
