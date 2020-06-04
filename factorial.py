def recursive_fact(n) :
    if n==1 :
        return 1
    else:
        return n*recursive_fact(n-1)


num=int(input('enter the no.'))
if (num<1):
    print('factorial doesnot exixt')
elif num==0 :
    print('the factorial of o is: 1')
else:
    print("the factorial of ",num, 'is',recursive_fact(num))

