import random

def rand_num(low, high,n):
    for i in range(n):
        yield random.randint(low, high)

i=0
for num in rand_num(1,10,12):
    i=i+1
    print(str(i)+"--->"+ str(num))