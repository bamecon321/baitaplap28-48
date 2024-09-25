# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:56:24 2024

@author: ACER
"""

S = 0
n = int(input("nhập n: "))
while n<0:
    n = int(input("nhập lại: "))
for i in range(1,n+1):
    S = S + 1 / (i*(i + 1))
print("S =", round(S,2))