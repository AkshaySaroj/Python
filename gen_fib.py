def gen_fib(n):
    a=1
    b=1
    for i in range(n):
        yield a
        a, b=b,a+b

for number in gen_fib(10):
    print(number)

 