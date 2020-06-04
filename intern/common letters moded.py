# The function is expected to return an integer.
# The function accepts an string array(list of input) and an integer(length of input) as parameters.

def logic(inputs, input_length):
    count=0
    temp=0
    str=inputs[0]
    for j in range(len(str)):
        for k in range(input_length):
            if str[j] in inputs[k]:
                print(str[j]+" findin "+inputs[k])
                temp+=1
                print(temp)
        if temp>=3:
            count+=1
        temp=0
    return count
            


# Do not edit below

# Get the input
input_length = int(input('Enter the input:'))
inputs = []
for x in range(input_length):
    inputs.append(input())

# Print output returned from the logic function
print(logic(inputs, input_length))
