#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: kk
# @Date:   2015-08-28 09:05:32
# @Last Modified by:   yuiwi
# @Last Modified time: 2017-08-26 11:51:48

import Lab03_3 as Lab03_3
import sys


for line in sys.stdin:
    line = line.rstrip('\n')
    nums = list(map(float, line.split()))
    x = nums[0]
    result = Lab03_3.octagon_area(x)
    print("%.6f" % result, type(result))
