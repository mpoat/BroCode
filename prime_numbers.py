
nums=range(1,1000)
#print(list(nums))

def is_prime(num):
    for x in range(, num):
        if (num % x) == 0:
            return False
    return True

primes = list(filter(is_prime, nums))
print(primes)

# The number 1 is NOT a prime number, this is wrong