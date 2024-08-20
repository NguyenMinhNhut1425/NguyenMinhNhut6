# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 18:57:49 2024

@author: MINH NHUT
"""

s = ('Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. Hồ Chí Minh')
s1 = s.replace('P. ','').replace('Q. ','').replace('Tp. ','').split(', ')
for i in s1:
    print(i)