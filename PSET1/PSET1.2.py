# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:51:47 2022

@author: DeeJay
"""

s = 'azcbobobegghakl'

b = True
c = 0

while b == True: 
    pos = s.find('bob')
    if pos == -1:
        b = False
        break
    s = s[pos+2:]
    c += 1

print('Number of times bob occurs is: ', c)