#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kk
# @Date:   2015-08-28 09:05:32
# @Last Modified by:   yuiwi
# @Last Modified time: 2017-08-26 11:53:02

import Lab03_5 as Lab03_5
import sys


for line in sys.stdin:
    line = line.rstrip('\n')
    nums = list(map(int, line.split()))
    number = nums[0]
    k = nums[1]
    value = nums[2]
    digit = Lab03_5.kth_digit(number, k)
    result = Lab03_5.set_kth_digit(number, k, value)
    print(digit, type(digit), result, type(result))
