import random

def probable_prime_test(target: int, attempts: int):
    if target%2 == 0:
        return "Ei alkuluku"
    (s, d)=factor_out(target-1)
    for i in range(attempts):
        a = random.randint(2,target-2)
        x = a%target
        for ii in range(1,d):
            x = (x*a)%target
        for iii in range (s):
            y = ((x%target)*x)%target
            if y == 1 and x != 1 and x != target-1:
                return "Ei alkuluku"
            x = y
        if y != 1:
            return "Ei alkuluku, hep"
    return "Luultavasti alkuluku"


def factor_out(number):
    i = 0
    while number%2 == 0:
        i += 1
        number /= 2
    return (i, int(number))
