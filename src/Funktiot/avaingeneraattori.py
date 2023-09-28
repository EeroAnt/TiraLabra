import Funktiot.alkulukugeneraattori as primegenerator
import random

def generate_key():
    p = primegenerator.generate_probable_prime(1024,40)
    q = primegenerator.generate_probable_prime(1024,40)
    while p == q:
        q = primegenerator.generate_probable_prime(1024,40)
    n = p*q
    lambda_n=lcm(p-1,q-1)
    while True:
        e = random.randint(100,min(lambda_n,10**5))
        if gcd(lambda_n,e) == 1:
            break
    d = extended_gcd(lambda_n,e)
    p,q,lambda_n=0
    return (n,e,d)

def lcm(a,b):
    return (a*b)/gcd(a,b)

def gcd(a,b):
    bigger = max(a,b)
    smaller = min(a,b)
    while True:
        q = 1
        while bigger >= (q+1)*smaller:
            q += 1
        (bigger, smaller) = (smaller,bigger-q*smaller)
        if smaller == 0:
            break
    return bigger

def extended_gcd(a,b):
    (old_r,r)=(a,b)
    (old_s,s)=(1,0)
    while r != 0:
        quotient = quotient_from_eucleidian_div(old_r, r)
        (old_r,r)=(r,old_r - quotient*r)
        (old_s,s)=(s,old_s - quotient*s)
    return old_s
    

def quotient_from_eucleidian_div(a,b):
    q = 0
    r = a
    while r > b:
        q += 1
        r -= b
    return q