import re
#\d equivalent to [0-9]
p =re.compile('\d')
print(p.findall('I went to him at 11 A.M on 4th July 1886'))

#\d+ will match a group on [0-9],group of one or greater size
p=re.compile('\d+')
print(p.findall('I went to him at 11 A.M on 4th July 1886'))

txt='The rain in Spain'
x=re.findall('portugal',txt)
if(x):
    print('there is match')
else:
    print('no match')

