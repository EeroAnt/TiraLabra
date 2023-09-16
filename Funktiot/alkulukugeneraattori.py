import Funktiot.alkulukutesti as test
import random

def generate_probable_prime(b, k):
    while True:
        number = random.randint(2**(b-1),(2**b)-1)
        if test.probable_prime_test(number,k) == "Luultavasti alkuluku":
            return number