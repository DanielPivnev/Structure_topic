import time
import math


# Решето Эратосфена
def eratosthenes(n, sieve=list(range(2, 100)), k=99):
    i = -1
    while True:
        i += 1
        while sieve[i] == 0:
            i += 1

        if sieve[i] * sieve[i] < len(sieve) + 2:
            for j in range((sieve[i] * sieve[i]) - 2, len(sieve)):
                if sieve[j] != 0 and sieve[i] != 0 and (sieve[j] / sieve[i]) % 1 == 0:
                    sieve[j] = 0
        else:
            break

    sieve1 = [x for x in sieve if x != 0]

    if n > len(sieve1):
        for i in range(100):
                sieve.append(k + 1)
                k += 1
        return eratosthenes(n, sieve, k)
    else:
        return sieve1[n - 1]


number = int(input('Enter please which i-th prime number you will get: '))

now = time.perf_counter()
print('There is it:', eratosthenes(number))
now1 = time.perf_counter()
print('Searching time:', now1 - now)


# Без решета Эратосфена
print('-' * 150)
prime_numbers = [2, 3, 5, 7]
b = 11
flag = True


now = time.perf_counter()
while number > len(prime_numbers):
    for i in range(int(math.sqrt(b))):
        if (b / prime_numbers[i]) % 1 == 0:
            flag = False
            break
    else:
        flag = True
    if flag:
        prime_numbers.append(b)
    b += 2
else:
    print('There is it:', prime_numbers[number - 1])
now1 = time.perf_counter()
print('Searching time:', now1 - now)
