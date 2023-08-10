def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            return True
    return False

nums = range(1, 101)
primes = filter(is_prime, nums)
print(list(primes))