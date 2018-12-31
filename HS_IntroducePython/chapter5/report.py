# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:24:05 2018

@author: INHA
"""

def get_description():
    """Return random weather, just like the pros"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sum', 'who knows']
    return choice(possibilities)