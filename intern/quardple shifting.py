# The function is expected to return a string.
# The function accepts string as parameter.

def logic(my_input):
    temp1=''

    list1=list(my_input)
    for i in range(0,len(my_input),4):
        if i+4>len(list1):
            break
        
        temp1=list1[i]
        list1[i]=list1[i+2]
        list1[i+2]=temp1
        temp1=list1[i+1]
        list1[i+1]=list1[i+3]
        list1[i+3]=temp1
    str=''
    for i in list1:  
        str += i  
    return str


# Do not edit below

# Get the input
my_input = input('enter the no:')

# Print output returned from the logic function
print(logic(my_input))
