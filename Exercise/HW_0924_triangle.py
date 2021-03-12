# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:43:03 2020

@author: clark
"""

#1
for idx in range(10, 0, -1):
    print("+" * idx)
#2
for idx in range(1, 11):
    print("+" * idx)    
#3
for idx in range(10,0,-1):
    print(" " * (idx-1) + "+" * (10-idx+1))
#4
for idx in range(1,11):
    print("+" * (10-idx+1) + " " * (idx-1))

#5
for idx in range(10, 0, -1):
    print(" " * idx+"+ "*(10-idx+1))
#6
for idx in range(10, 0, -1):
    print(" " * (10-idx+1) +"+ "*(idx))
   