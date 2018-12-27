# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 10:29:56 2018

@author: admin
"""
import tensorflow as tf

def weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial=tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

def conv_layer(x,shape):
    W=weight_variable(shape)
    b=bias_variable([shape[3]])
    return tf.nn.relu(conv2d(x,W)+b)

def full_layer(x,size):
    in_size=int(x.get_shape()[1])
    W=weight_variable([in_size,size])
    b=bias_variable([size])
    return tf.matmul(x,W)+b