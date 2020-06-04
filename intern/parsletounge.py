# The function is expected to return a string.
# The function accepts string as parameter.

def logic(my_input):
    temp=0
    s_count=0
    for i in range(len(my_input)):
        if my_input[i].lower()=='s':
            s_count+=1
            if my_input[i].lower()=='s' and my_input[i+1].lower()=='s':
                temp+=1


        
    if temp>=2 or s_count<1:
        return "yes"
    else:
        return "no"


'''
input : 
sShe is good at sshooting

output: Yes

Input : It is nothing good
Output: No
'''

# Get the input
my_input = input('enter the:')

# Print output returned from the logic function
print(logic(my_input))

