# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:37:15 2024

@author: ACER
"""

S = 1
n = int(input("nhập n: "))
while n<0: 
    n = int(input("nhập lại: "))
for i in range(1,n+1):
    S += 1/(2*i + 1)
print("S =", round(S,2))