import random

def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    def miller_test(d, n):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for _ in range(k):
        if not miller_test(d, n):
            return False
    return True


print(miller_rabin(29))
print(miller_rabin(15))

'''
Key Points:
	•	Adjustable Accuracy: The parameter k determines the number of rounds of testing. Increasing k increases the accuracy.
	•	Probabilistic Nature: The test is probabilistic, meaning there’s a very small chance it might incorrectly identify a
    composite number as prime. However, with a reasonable k value (e.g., 5 or 10), the error rate becomes negligibly small.
'''


# EXTRAS

## Checking divisibility only up to the square root of the number:
'''
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(29))
print(is_prime(15))
'''


## Fermat’s Little Theorem:


'''
def fermat_little_theorem(a, p):
    return pow(a, p - 1, p) == 1

print(fermat_little_theorem(2, 17))
print(fermat_little_theorem(5, 17))
'''

## Sieve of Eratosthenes:


'''
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
    return prime_numbers
'''


## Trial Division:

'''
def trial_division(n):
    primes = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            primes.append(i)
            if i != n // i:
                primes.append(n // i)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
'''