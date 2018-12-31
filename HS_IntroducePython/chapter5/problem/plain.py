# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:40:32 2018

@author: INHA
"""


plain = {'a':1, 'b':2, 'c':3}
print(plain)

from collections import OrderedDict
fancy = dict()

for key, value in plain.items():
    fancy[key] = value

fancy = OrderedDict(fancy)
print(fancy)


from collections import defaultdict

dict_of_lists = defaultdict(list)
dict_of_lists['a'] = ['something for a']

print(dict_of_lists)
