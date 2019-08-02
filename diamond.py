#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input('输入行数：'))

# 第一种方法
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))

for i in range(1,n):
    print(' '*i+'*'*(2*n -2 -(2*i -1)))

# 第二种方法，打印出来的菱形比第一种方法小一半
import math

nn = math.ceil(n/2)
print(nn)
for i in range(1,n+1):
    print(' '*abs(nn-i)+'*'*(2*abs(nn-abs(nn-i))-1))
