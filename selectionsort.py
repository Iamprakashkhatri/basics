def SelectionSort(array1,n):
    for i in range(n):
        for j in range(i+1,n):
            if(array1[i]>array1[j]):
                temp=array1[i]
                array1[i]=array1[j]
                array1[j]=temp
    print(array1)

n=int(input("enter the no. of element for array:"))
array1=list()
for i in range(n):
    lists= input('enter the elements of array:')
    array1.append(int(lists))

SelectionSort(array1,n)
