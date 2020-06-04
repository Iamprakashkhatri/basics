
# Take an array and target number from user, sum up two array number to get target number.Return index for those two number.

def sum(array1,target_no,n):
    for i in range(n):
        for j in range(i+1,n):
            if(array1[i]+array1[j]==target_no):
                return (i,j)

target_no=int(input('enter the target no:'))
n=int(input("enter the no. of element for array:"))
array1=list()
for i in range(n):
    lists= input('enter the elements of array:')
    array1.append(int(lists))

print(sum(array1,target_no,n))
