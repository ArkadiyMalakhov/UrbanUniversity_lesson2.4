numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    if i > 1:
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                is_prime = False
                not_primes.append(i)
                break
        else:
            primes.append(i)
print(f'primes= {primes}')
print(f'not_primes= {not_primes}')

