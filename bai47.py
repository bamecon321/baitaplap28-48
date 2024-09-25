# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 23:48:40 2024

@author: ACER
"""

bo_nghiem = []
max = 979
for x in range(1,490):
    for y in range(1, 140):
        for z in range(1, 109):
            if 2*x + 7 *y + 9*z == 979:
                sum = x + y + z
                if sum > max:
                    max = sum
                    bo_nghiem=[(x,y,z)]
print(f"(bo_nghiem) co tri lon nhat x + y + z = {max}")