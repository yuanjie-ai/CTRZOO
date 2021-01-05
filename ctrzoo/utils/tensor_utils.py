#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : inn.
# @File         : tensor_utils
# @Time         : 2020/5/20 10:59 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  :

import numpy as np
import tensorflow as tf


def arr2sparse(arr):
    arr_tensor = tf.constant(np.array(arr))
    arr_idx = tf.where(tf.not_equal(arr_tensor, 0))
    arr_sparse = tf.SparseTensor(arr_idx, tf.gather_nd(arr_tensor, arr_idx), arr_tensor.get_shape())
    return arr_sparse


def sparse2dense(tensor):
    return tf.sparse.to_dense(tensor)
