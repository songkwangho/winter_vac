# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:56:12 2018

@author: INHA
"""

if(1):
    
# 7.1
    import unicodedata
    
    mystery = '\U0001f4a9'
    print(mystery)
    print(unicodedata.name(mystery))

# 7.2
    pop_bytes = mystery.encode('UTF-8')
    print(pop_bytes)
    
# 7.3
    pop_string = pop_bytes.decode('UTF-8')
    print(pop_string)
    
# 7.4
    print("""My kitty cat likes %s, 
          My kittycat likes %s, 
          My kitty cat fell on his %s
          And now thinks he's a %s""" % ('roast beef', 'ham', 'head', 'clam'))
    
# 7.5
    letter = """Dear {salutation} {name},
          Thank you for your letter. We are sorry that our {product} {verbed} in your
          {room}. Please note that it should never be used in a {room}, espectially
          near any {animals}.
          
          Send us your receipt and {amount} for shipping and handling. We will send
          you another {product} that, in our tests, is {percent}% less likely to
          have {verbed}.
          
          Thank you for your support.
          
          Sincerely,
          {spokesman}
          {job_title}"""
          
# 7.6
    response_dict = {'salutation': '★', 'name': '★','product' : '★','verbed' : '★','room':'★',
                     'animals': '★', 'amount':'★', 'percent': '★', 'spokesman': '★', 'job_title':'★'}
    print(letter.format(**response_dict)) # ** 의 효과 공부해볼것
    
# 7.7
    mammoth = """We have seen the Queen of cheese, 
Laying quietly at your ease, 
Gently fanned by evening breeze,  
Thy fair form no flies dare seize. 

All gaily dressed soon you'll go 
To the great Provincial show, 
To be admired by many a beau 
In the city of Toronto. 

Cows numerous as a swarm of bees,
Or as the leaves upon the trees, 
It did require to make thee please, 
And stand unrivalled Queen of Cheese. 

May you not receive a scar as 
We have heard that Mr. Harris 
Intends to send you off as far as 
The great World's show at Paris. 

Of the youth beware of these, 
For some of them might rudely squeeze 
And bite your cheek; then songs or glees 
We could not sing o' Queen of Cheese. 

We'rt thou suspended from baloon, 
You'd cast a shade, even at noon, 
Folks would think it was the moon 
About to fall and crush them soon."""
    
# 7.8
    import re
    pat = r'\bc\w*'     # r = \b 가 백스페이스로 인식되는것을 막아줌
                        # \b = 단어의 경계
                        # \w = 알파벳 문자
                        # * = 0회 이상
                        # 단어시작이 c 이고 c의 뒤에 알파벳 문자가 0회이상 
                        # \b 안써도 되는데 왜 써야하는가?
    print(re.findall(pat,mammoth))
    
    # e로 끝나는 단어를 해보자.
    pat2 = r'\w*e\b'
    print(re.findall(pat2,mammoth))
    # a 가 포함된 단어
    pat3 = r'\w*a\w*'
    print(re.findall(pat3,mammoth))
    # n으로 끝나는 단어
    pat4 = r'\w*n\b'
    print(re.findall(pat4,mammoth))
    
# 7.9
    pat5 = r'\bc\w{3}\b'     # /w{3} 알파벳 3글자
    print(re.findall(pat5,mammoth))
    
# 7.10
    pat6 = r'\w*r\b'
    print(re.findall(pat6,mammoth))
    
# 7.11
    pat7 = r'\w*[aeiou]{3}\w*'    # 답은 뭔가 더 복잡했음... 질문해야겠음
    print(re.findall(pat7,mammoth))
    
# 7.12
    import binascii
    hex_str = '47494638396101000100800000000000ffffff21f9' + '0401000000002c000000000100010000020144003b'
    gif = binascii.unhexlify(hex_str)
    print(len(gif))    # 왜 길이를 출력하는가?
    
# 7.13
    print(gif[:6])
    
# 7.14
    print(gif)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    