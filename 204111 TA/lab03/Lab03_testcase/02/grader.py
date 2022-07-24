#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kk
# @Date:   2015-08-28 09:05:32
# @Last Modified by:   yuiwi
# @Last Modified time: 2017-08-26 11:45:49

import Lab03_2 as Lab03_2
import sys


for line in sys.stdin:
    line = line.rstrip('\n')
    nums = list(map(int, line.split()))
    x = nums[0]
    result = Lab03_2.reverse_digits(x)
    print(result)
    print(type(result))
