n = int(input("sayı gir: "))
primes = []
count = 2
for i in range(2, n + 1):
    for j in range(2, i-1):
         if i%j == 0:
            break
    else:
        primes.append(i)

print(primes)
