# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:52:44 2020

@author: clark
"""
num = int(input('Please enter a number:'))
i = num
j = 2
if (num > 1):
    while (j < i):
        if (i % j == 0):
            i -= 1
        else:
            j += 1
            if (j == i):
                print(f'{num}的最大質數為{i}')
                break
else:
    print('找不到質數')