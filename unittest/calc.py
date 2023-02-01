# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:55:01 2021

@author: ASUS
"""

def add(x,y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract function"""
    return x - y

def multiplication(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError('Can not divide by Zero')
    return x / y
