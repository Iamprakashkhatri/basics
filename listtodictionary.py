def Convert(lst): 
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)} 
    return res_dct 
          
# Driver code 
lst = ['a', 1, 'b', 2, 'c', 3] 
print(Convert(lst)) 

list=[1,2,3,4]
for i in range(0,len(list)):
    print(i)
lst = ['a', 1, 'b', 2, 'c', 3,None] 
p={ lst[i]:lst[i+1] for i in range(0,len(lst)-1)}
print(p)