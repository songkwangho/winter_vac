# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 21:45:17 2018

@author: INHA
"""
if(1):
    
# 6.1
    class Thing():
        pass
    
    print(Thing)
    
    example = Thing()
    print(example)

# 6.2
    class Thing2():
        letters = 'abc'
    print(Thing2.letters)

# 6.3
    class Thing3():
        def __init__(self):
            self.letters = 'xyz'
    
    thing = Thing3()    
    print(thing.letters)
    
# 6.4
    class Element():
        def __init__(self,name,symbol,number):
            self.name = name
            self.symbol = symbol
            self.number = number
            
        
    
    hydrogen = Element('Hydrogen', 'H', 1)
    print(hydrogen.name)
    print(hydrogen.symbol)
    print(hydrogen.number)
    
# 6.5
    el_dict = {'name':'Hydrogen', 'symbol':'H','number':1}
    
    hydrogen_from_dict = Element(el_dict.get('name'),el_dict.get('symbol'),el_dict.get('number'))
    
    print(hydrogen_from_dict.name)
    print(hydrogen_from_dict.symbol)
    print(hydrogen_from_dict.number)
    
# 6.6
    class Element2():
        def __init__(self,name,symbol,number):
            self.name = name
            self.symbol = symbol
            self.number = number
             
        def dump(self):
            print("it's dump !")
            print(self.name)
            print(self.symbol)
            print(self.number)
            
    hydrogen2 = Element2(**el_dict)
    hydrogen2.dump()
    
# 6.7
    print(hydrogen2)
    class Element2():
        def __init__(self,name,symbol,number):
            self.name = name
            self.symbol = symbol
            self.number = number
             
        def __str__(self):
            print("it's str !")
            print(self.name)
            print(self.symbol)
            print(self.number)
            return ''
    
    hydrogen2 = Element2(**el_dict)
    print(hydrogen2)
    
# 6.8
    class Element3():
        def __init__(self,name,symbol,number):
            self.name = name
            self.symbol = symbol
            self.number = number
             
        def __str__(self):
            print("it's str !")
            print(self.name)
            print(self.symbol)
            print(self.number)
            return ''
    
# 6.9
    class Bear():
        def eats(self):
            return 'berries'

    class Rabbit():
        def eats(self):
            return 'clover'

    class Octothorpe():
        def eats(self):
            return 'campers'
    
    bear = Bear()
    rabbit = Rabbit()
    octothorpe = Octothorpe()
    
    print('Bear eats %s, Rabbit eats %s, Octothorpe eats %s' 
          % (bear.eats(),rabbit.eats(),octothorpe.eats()))
          
# 6.10
    class Laser:
        def does(self):
            return 'disintegrate'
        
    class Claw:
        def does(self):
            return 'crush'
        
    class Smart_phone():
        def does(self):
            return 'ring'
        
    class Robot:
        def __init__(self):
            self.laser = Laser()
            self.claw = Claw()
            self.smart_phone = Smart_phone()
        
        def does(self):
            print('my laser : %s, my claw : %s, my smart_phone : %s' 
                  % (self.laser.does(),self.claw.does(),self.smart_phone.does()))
    
    robot = Robot()
    robot.does()
              
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          