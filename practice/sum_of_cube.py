def sum_of_cube(num):
    n=num-1
    total=0
    for i in range(n,0,-1):
        total=i*i*i + total
        print('i',i,total)
    print(total)

sum_of_cube(6)
