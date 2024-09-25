# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:01:26 2024

@author: ACER
"""

a = float(input("Nhap vao so km: "))
if a <= 1 :
    print(" So tien la: ", a*15)
elif 2 <= a <= 5:
    print("So tien la: ", 1*15 + ((a-1)*13.5))
else:
    print("So tien la: ", 1*15 + 4*13.5 + (a-5)*11)
    t=1*15 + 4*13.5 + (a-5)*11
if a >=120 :
    print("So tien la: ", t*0.9)