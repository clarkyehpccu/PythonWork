# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:43:03 2020

@author: clark
"""
n = int(input("Input number N to get the max prime less than N:"))
for idx1 in range(n-1, 1, -1):
    flag_prime = 1
    for idx2 in range(idx1//2, 1, -1):
        if idx1%idx2 == 0 :
           flag_prime = 0
           break
    if flag_prime == 1:
        print(idx1, " is the max prime less than", n)
        break
       