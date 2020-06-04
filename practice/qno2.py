# The function is expected to return a string.
# The function accepts string as parameter.

def logic(my_input):
    my_string =''
    for i in range(len(str(my_input))-1):
        if my_input[i]>my_input[i+1]:
            my_string=my_string+my_input[i]
        elif my_input[i]<my_input[i+1]:
            my_string=my_string+my_input[i+1]
        elif my_input[i]==my_input[i+1]:
            my_string=''
    if my_string=='':
        return 'total carnage'
    else:
        return int(my_string)
            

'''
input1: 5879445
output: 895

input:558899
output: 'total carnage
'''


# Do not edit below

# Get the input
my_input = input('enter the string:')

# Print output returned from the logic function
print(logic(my_input))
