# Asal sayı kontrol fonksiyonu
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 1'den 100'e kadar sayıları dosya.txt'ye yazma
with open('dosya.txt', 'w') as f:
    for i in range(1, 101):
        f.write(f"{i}\n")

# Sayıları asal ve asal olmayan olarak ayırma
with open('dosya.txt', 'r') as f:
    primes = []
    non_primes = []
    for line in f:
        number = int(line.strip())
        if is_prime(number):
            primes.append(number)
        else:
            non_primes.append(number)

# Asal sayıları asal_sayilar.txt dosyasına yazma
with open('asal_sayilar.txt', 'w') as f:
    for prime in primes:
        f.write(f"{prime}\n")

# Asal olmayan sayıları asal_olmayan_sayilar.txt dosyasına yazma
with open('asal_olmayan_sayilar.txt', 'w') as f:
    for non_prime in non_primes:
        f.write(f"{non_prime}\n")