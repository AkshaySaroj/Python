def create_cubes(n):
   ''' result=[]
    for x in range(n):
        result.append(x**3)
    return result
    '''
   for x in range(n):
       yield x**3

print(create_cubes(10))


for x in create_cubes(10):

    print(x)