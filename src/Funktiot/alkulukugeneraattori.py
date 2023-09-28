import Funktiot.alkulukutesti as test
import random

def generate_probable_prime(b, k):
    first_primes = test.first_primes()
    i = 0
    while True:
        i += 1
        number = random.randrange(2**(b-1)+1,(2**b)-1,2)
        if test.probable_prime_test(number,k, first_primes):
            print(test.is_prime(number))
            return number
        print(i)