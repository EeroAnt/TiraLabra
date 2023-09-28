import random
import math

def probable_prime_test(target: int, attempts: int, first_primes: list):
    for i in first_primes:
        if target%i == 0:
            return "Ei alkuluku, jaollinen pienellä alkuluvulla"
    (s, d)=factor_out(target-1)
    for ii in range(attempts):
        a = random.randint(1009,target-2)
        x = pow(a,d,target)
        for iii in range(s):
            y = pow(x,2,target)
            if y == 1 and x !=1 and x != target-1:
                return "Ei alkuluku"
            x = y
        # if y != 1:                tämä klausaali nähtävästi tuotti hitautta. en tiedä saako sen poistaa toisaalta
        #     return "Ei alkuluku"
    return "Luultavasti alkuluku"

def factor_out(number):
    i = 0
    while number%2 == 0:
        i += 1
        number /= 2
    return (i, int(number))

def first_primes():
    primes = [2]
    prime_candidate = 3
    while prime_candidate < 1000:
        not_a_prime = False
        for i in primes:
            if i <= math.sqrt(prime_candidate)+1:
                if prime_candidate%i == 0:
                    not_a_prime = True
                    break
        if not not_a_prime:
            primes.append(prime_candidate)
        prime_candidate += 2
    return primes