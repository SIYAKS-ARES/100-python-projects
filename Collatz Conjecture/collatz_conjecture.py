import random

def collatz_conjecture():
    num = random.randint(1, 100000)
    print(f"Starting number: {num}")

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(num)

collatz_conjecture()