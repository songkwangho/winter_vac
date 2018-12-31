# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:44:21 2018

@author: INHA
"""

from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)