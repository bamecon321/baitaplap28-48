# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:55:33 2024

@author: ACER
"""

a = int(input("Nhap so N nguyen duong: "))
tong = 0
while a > 0:
    tong = tong + a % 10
    a = a // 10
print("Tong cac chu so la: ", tong)
    
