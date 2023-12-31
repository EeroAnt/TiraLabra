import random
import math
import Funktiot.matikkapalikat as mathaid

# probable_prime_test tapailee Miller-Rabin algoritmia. Karsin kuitenkin ensin
# kaikki luvut pois, jotka jaollisia luvuilla 1000 ja alaspäin. Factor_out
# jakaa parillisen luvun kahden potensseihin ja parittomaan tekijään, joilla
# Miller-Rabin toimii


def _probable_prime_test(target: int, attempts: int, first_primes: list):
    for i in first_primes:
        if target%i == 0:
            return False
    (s, d)=mathaid._factor_out(target-1)
    for ii in range(attempts):
        a = random.randint(2,target-1)
        x = pow(a,d,target)
        for iii in range(s):
            y = pow(x,2,target)
            if y == 1 and x !=1 and x != target-1:
                return False
            x = y
        if y != 1:
            return False
    return True

def _first_primes():
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
