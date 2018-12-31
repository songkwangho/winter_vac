# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:04:27 2018

@author: INHA
"""

from collections import defaultdict, Counter
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1
    
for food, count in food_counter.items():
    print(food, count)
    
list_food = ['spam', 'tomato', 'eggs', 'tomato', 'eggs', 'tomato']
list_food += ['spam', 'tomato', 'eggs', 'tomato', 'eggs', 'tomato']

list_food_counter = Counter(list_food)
print(list_food_counter.most_common())