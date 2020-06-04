from bisect import bisect_right

n = int(input('enter score:'))
scores=sorted(set([int(x) for x in input().split()]))
print(scores)
# scores = sorted(set(map(int,input().split())))

m = int(input('enter the value of alice:'))
alice=[int(x) for x in input().split()]
# alice = map(int,input().split())
print(alice)

# your code goes here

''' 
comments:
# initializing list 
li = [1, 3, 4, 4, 4, 6,6, 7] 
  
# using bisect() to find index to insert new element 
# returns 5 ( right most possible index ) 
print ("The rightmost index to insert, so list remains sorted is  : ", end="") 
print (bisect.bisect_left(li, 4)) 

'''
for i in alice:
    print(len(scores)-bisect_right(scores,i)+1)