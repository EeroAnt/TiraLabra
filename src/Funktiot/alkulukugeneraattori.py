import Funktiot.alkulukutesti as test
import random

def generate_probable_prime(b, k):
    first_primes = test.first_primes()
    while True:
        number = random.randint(2**(b-1),(2**b)-1)
        if test.probable_prime_test(number,k, first_primes) == "Luultavasti alkuluku":
            return number