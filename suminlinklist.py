'''
input: 
link_list1=5->6->3 //563
link_list2=8->4->2 //842

output:
   result: 1->4->0->5

'''

link_list1={5:6,6:3,3:None}
link_list2={8:4,4:2,2:None}

list1=''
for key in link_list1.keys():
    list1=list1 + str(key)
print(list1)

list2=''
for key in link_list2.keys():
    list2=list2 + str(key)
print(list2)

list3 = int(list1[::-1]) + int(list2[::-1])
print(list3)

res = [int(x) for x in str(list3)]
res.append('')
print(res)
# list4=list(str(list3))
# print(list4.append('null'))

p={ res[i]:res[i+1]  for i in range(0,len(res)-1)}
print(p)

