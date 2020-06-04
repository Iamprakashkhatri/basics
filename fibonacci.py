nterms=int(input('enter the no.'))

n1=0
n2=1
count=0

if nterms<1 :
    print ("enter the positive no.")
elif nterms==1 :
    print(n1)
else:
    print(n1,',',n2,end=',')
    while count<nterms:
        nth=n1+n2
        print(nth,end=',')
        count=count+1
        n1=n2
        n2=nth