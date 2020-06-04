def bubbleSort(array1,n):
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(array1[j]>array1[j + 1]):
                temp=array1[j]
                array1[j]=array1[j+1]
                array1[j+1]=temp
    print(array1)

n=int(input("enter the no. of element for array:"))
array1=list()
for i in range(n):
    lists= input('enter the elements of array:')
    array1.append(int(lists))

bubbleSort(array1,n)

# def calValue(num,list1):
#     for i in range(0,num):
#         for j in range(0,num-i-1):
#             if (list1[j]>list1[j+1]) :
#                 temp=list1[j]
#                 list1[j]=list1[j+1]
#                 list1[j+1]=temp
#     return list1

# num=int(input('enter the value of n for list:'))
# list1=list()
# for i in range(0,num):
#     list=input('enter the element for list:')
#     list1.append(int(list))
# # target_no=int(input('enter the target no:'))

# print(calValue(num,list1))