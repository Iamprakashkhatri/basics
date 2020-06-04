num=int(input("enter the no:"))
for i in range(2,num):
    if num%i==0 :
        print('the no is not prime')
        break
else:
    print('the no is prime')