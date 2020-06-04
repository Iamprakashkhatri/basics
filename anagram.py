from collections import Counter

def anagram(input1,input2):
    if Counter(input1)==Counter(input2):
        return True
    else:
        return False
input1='abcd'
input2='cdae'
print(anagram(input1,input2))