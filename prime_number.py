import math

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True

num = int(input())

is_num_prime = is_prime(num)

if is_num_prime:
    print("prime")
else:
    print("not a prime")
