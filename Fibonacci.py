fib = []
a = 0
b = 1
while b < 56 :
    fib.append(b)
    c = a + b
    a = b
    b = c
print(fib)
