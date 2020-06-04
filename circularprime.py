import math
def isPrime(n):
    for i in range(2,n):
        if n%i==0 :
            return False
    else:
        return True

def checkCircular(N):
    count=0
    temp=N
    counter=len(str(N))
    while(temp>0):
        count=count+1
        temp=temp//10
    num=N
    while(isPrime(num)):
        rem=num%10
        div=num//10
        num=(int((math.pow(10,counter-1)*rem)+div))
    if(num==N):
        return True
N=113
print(checkCircular(N))
