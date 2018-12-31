# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:52:26 2018

@author: INHA
"""

periodic_table = {'Hyderogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)

print(periodic_table)


from collections import defaultdict
periodic_table = defaultdict(int)

periodic_table['Hydrogen'] = 1
periodic_table['Lead']

print(periodic_table)