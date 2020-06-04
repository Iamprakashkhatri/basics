#WAP to calculate maximum votes. If two person got equal vote then print that person whose name is alphabetically smaller


from collections import Counter
def winner(input):
    votes=Counter(input)
    print(votes)
    dict={}
    for value in votes.values():
        dict[value]=[]
    print(dict)
    for k,v in votes.items():
        dict[v].append(k)
    print(dict)

    maxvote=sorted(dict.keys(),reverse=True)[0]
    print(maxvote)
    if len(dict[maxvote])>1:
        print(dict[maxvote])
        print (sorted(dict[maxvote])[0])
    else:
        print (dict[maxvote])


input=['AAA','BBB','CCC','AAA','BBB','DDD']
winner(input)