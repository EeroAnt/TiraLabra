import Funktiot.alkulukutesti as test
import random

# Funktio arpoo parittomia oikean pituisia lukuja ja tarkistaa
# onko todennäköinen alkuluku. Jos on, palautuu kyseinen luku.
# Jos ei ole, arvotaan uusi luku testiin. 


def generate_probable_prime(b, k):
    first_primes = test.first_primes()
    while True:
        number = random.randrange(2**(b-1)+1,(2**b)-1,2)
        if test.probable_prime_test(number,k, first_primes):
            return number