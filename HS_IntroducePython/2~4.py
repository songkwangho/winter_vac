# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:23:09 2018

@author: INHA
"""
if(1): # 한줄 띄우려고 씀


# 2.1 
    print('1 hour is %d minute %d second' %( 60, 60*60))

# 2.2
    seconds_per_hour = 60*60

# 2.3
    print('1 day is %d hour %d minute %d second' %(24, seconds_per_hour/60*24, seconds_per_hour*24))

# 2.4
    seconds_per_day = seconds_per_hour*24

# 2.5
    print('seconds_per_day / seconds_per_hour = ',seconds_per_day/seconds_per_hour)

# 2.6
    print('seconds_per_day // seconds_per_hour = ',seconds_per_day//seconds_per_hour)

# 3.1
    year_list = [1980]

    for i in range(1,6):
        year_list.append(year_list[0]+i)

    print(year_list)

# 3.2
    print('세번째 생일년도', year_list[3])

# 3.3
    print('가장 나이가 많을 때의 년도', year_list[-1])

# 3.4
    things = ['mozzarella', 'cinderella', 'salmonella']
    print(things)

# 3.5
    things[1] = things[1].capitalize()
    print(things)

# 3.6
    things[0] = things[0].upper()
    print(things)

# 3.7
    things.remove('salmonella')
    print(things)

# 3.8
    surprise = ['Groucho', 'Chico', 'Harpo']
    print(surprise)

# 3.9
    surprise[-1] = surprise[-1].lower()
    surprise[-1] = surprise[-1][::-1]
    surprise[-1] = surprise[-1].capitalize()
    print(surprise)

# 3.10
    e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
    print(e2f)
    
# 3.11
    print(e2f['walrus'])

# 3.12
    f2e = {}
    for english, french in e2f.items():
        f2e[french] = english
    
    print(f2e)

# 3.13
    print(f2e['chien'])

# 3.14
    print(e2f.keys())

# 3.15
    life = {'animals' : {'cats' : 'Henri', 'octopi' : 'Grumpy', 'emus' : 'Lucy'},'plants' : '', 'other' : ''}
    print(life)
    
# 3.16
    print(life.keys())

# 3.17
    print(life['animals'].keys())

# 3.18
    print(life['animals']['cats'])

# 4.1
    guess_me = 7
    if(guess_me <7):
        print('too low')
    elif(guess_me > 7):
        print('too high')
    else:
        print('just right')
        
# 4.2
    start = 1
    while(1):
        if(start < guess_me):
            print('too low')
        elif(start == guess_me):
            print('found it!')
            break
        elif(start > guess_me):
            print('oops')
        start += 1
        
    
# 4.3
    list_3to0 = [3, 2, 1, 0]
    for i in list_3to0:
        print(i)
# more pythonic
    list_3to0_2 = [i for i in range(3,0,-1)]
    for i in list_3to0_2:
        print('4.3-2', i)

# 4.4
    even_list = []
    for i in range(0,10,2):
        odd_list.append(i)
    print(even_list)
# more pythonic
    even_list2 = [i for i in range(0,10,2)]
    print('4.4-2 ', even_list2)

# 4.5
    squares = dict()
    for i in range(10):
        squares[i] = i**2
    print(squares)
# more pythonic
    squares2 = {i:i**2 for i in range(10)}
    print('4.5-2 ', squares2)

# 4.6
    myset = set()
    for i in range(0,10,2):
        myset.add(i+1)
    print(myset)
# more pythonic
    myset_2 = {i+1 for i in range(0,10,2)}
    print('4.6-2', myset_2)


# 4.7
    for i in range(10):
        print('Got', i)
        
# 4.8
    def good():
        return['Harry', 'Ron', 'Hermione']
    
    print(good())

# 4.9
    def get_odds():
        odd_list = []
        for i in range(0,10,2):
            odd_list.append(i+1)
        return odd_list
    
    print(get_odds()[2])
    
# 4.10
    
    def func():
        print('I am a func')
    
    def print_it(func):
        print('start')
        func()
        print('end')
    
    print_it(func)
    
# 4.11       나중에 보완해봐야겠다.
    class OopsException(Exception):
        print('Caught an oops')
    
    try:
        oops_list = [0, 1, 2]
        oops_list[7]
    except:
        OopsException()

# 4.12
    titles = ['Creature of Habit', 'Crewel Fate']
    plots = ['A nun turns into a monster', 'A haunted yarn shop']
    zip_movies = zip(titles,plots)
    movies = dict()
    for i, j in zip_movies:
        movies[i] = j
    
    print(movies)


