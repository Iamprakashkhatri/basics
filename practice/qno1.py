# The function is expected to return a string.
# The function accepts string as parameter.
import re

def logic(my_input):
    
    search1=re.search('\s',my_input)
    if search1:
        replaced =re.sub('x','cks',my_input)
        return (replaced)
    else:
        replaced1 = re.sub(r'^x', 'z', my_input)
        replaced2=re.sub('x','ecks',replaced1)
        return replaced2


'''
input1:xphone
output:zphone

x=ecks
input2:phonexcent
output2:phoneeckscent

input3:x ray
output3: eck ray

'''

    
# Get the input
my_input = input('enter the string:')

# Print output returned from the logic function
print(logic(my_input))
