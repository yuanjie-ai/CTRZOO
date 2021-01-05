#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : inn.
# @File         : smooth_utils
# @Time         : 2020/5/20 10:40 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import numpy as np


def walson_ctr(num_click, num_pv, z=1.96):
    """:arg
    威尔逊
    https://mp.weixin.qq.com/s/rLP1wsS0a71q5RA7NQcjdQ
    """
    p = num_click / num_pv
    if p > 0.9:
        return 0.0

    n = num_pv

    A = p + z ** 2 / (2 * n)
    B = np.sqrt(p * (1 - p) / n + z ** 2 / (4 * (n ** 2)))
    C = z * B

    D = 1 + z ** 2 / n

    ctr = (A - C) / D

    return ctr
