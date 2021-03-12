# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:43:03 2020

@author: clark
"""
x = 1
while x <= 9:
    y= 1
    while y <=9:
        print("{0:2d} X {1:2d} = {2:2d}".format(x, y, x*y))
        y += 1
    x += 1
       