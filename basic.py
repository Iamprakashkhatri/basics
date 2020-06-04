lis=1
li=[lis,lis+1]
for l in li:
    print(l)

reply=44
print(reply)

reply_qs=None
replys=[reply,reply+1]
for reply in replys:
    print(reply)


phase="Giraffe Academy"
print(phase + " is   cool")
print(phase.upper())
print(phase.isupper())
print(pow(3,2))
from math import *
print(floor(3.7))

b=[1,2,3]
print(b[1:])
from random import random
for  i in range(10):
    value=random()
    print(value)
import random
def roll_dice(num):
    return random.randint(1,num)
print(roll_dice(9))

i=1
while i<=10:
    i=i+1
print(i)

class Robot:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi, I am " + self.name)
class PhysicianRobot(Robot): #Inheriting Robot Properties
    pass
x = Robot("Marvin")
x.say_hi()
y = PhysicianRobot("James")
y.say_hi()

# tuple
list = []
apple='app'
banana='ban'
list.append({
    'apple':apple,
    'banana':banana,
},
)
for k,v in enumerate(list):
    print(v['apple'])


# dictionary
d={}
for x in range(1,21):
    d[x]=x**2
print(d.keys())
print(d.values())

apple='app'
banana='ban'
d={
    'apple':apple,
    'banana':banana,
}
for index,item in enumerate(d):
    print('enumerate:',)
for k,v in d.items():
    print(v)


dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(dict_num.keys())

list='prakash'
print(list.replace('prakash','santosh'))
