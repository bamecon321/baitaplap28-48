# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:35:16 2024

@author: ACER
"""

N = int(input("Nhap so nguyen duong N: "))
while N <= 0:
    print("Số N phải là số nguyên dương.")
    N = int(input("Nhập lại : "))


for i in range(1, N+1):
    if N % i == 0:
        print(i, end=" \t")
