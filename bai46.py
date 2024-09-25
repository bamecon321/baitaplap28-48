# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:43:43 2024

@author: ACER
"""

bo_nghiem = []
for x in range (1,490):
    for y in range (1, 140):
        for z in range (1, 109):
            if 2*x + 7*y + 9*z == 979:
                bo_nghiem = [(x,y,z)]
print(bo_nghiem)
                