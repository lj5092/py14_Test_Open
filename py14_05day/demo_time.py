#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/2 11:10 上午
# @Author  : LiangJun
# @Filename    : demo_time.py

import time

a = time.time()
for i in range(11):
    print(i)
b = time.time()

c = b-a

print(c)