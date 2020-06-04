# The function is expected to return an integer.
# The function accepts an string array(list of input) and an integer(length of input) as parameters.

def logic(inputs, input_length):
    alphabet='abcdefghijklmnopqurstuvwxyz'
    count=0
    temp=0
    for word in inputs:
        for j in range(len(word)):
            for k in range(input_length):
                if word[j] in inputs[k]:
                    temp+=1
        if temp>=3:
            count+=1
            temp=0
    return count
            


# Do not edit below

# Get the input
input_length = int(input())
inputs = []
for x in range(input_length):
    inputs.append(input())

# Print output returned from the logic function
print(logic(inputs, input_length))
