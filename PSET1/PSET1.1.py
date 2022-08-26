# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 18:51:47 2022

@author: DeeJay
"""

s = 'azcbobobegghakl'

c = 0
for i in s:
    for iv in 'aeiou':
        if not i == iv: continue
        else: c += 1
print(f'Number of vowels: {c}')