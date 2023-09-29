import Funktiot.alkulukugeneraattori as primegenerator
import random

# RSA-avain koostuu modulosta (n), salauseksponentista (e) ja
# purkueksponentista (d). n on yksinkertaisesti 2 suuren alkuluvun
# tulo. Ja loput lasketaan alla olevilla funktioilla. p, q ja
# lambda_n nollataan varuilta. Niiden avulla voisi laskea avaimen 
# salaisen osan.

def _generate_key():
    p = primegenerator._generate_probable_prime(1024,40)
    q = primegenerator._generate_probable_prime(1024,40)
    while p == q:
        q = primegenerator._generate_probable_prime(1024,40)
    n = p*q
    lambda_n=_lcm(p-1,q-1)
    while True:
        e = random.randint(100,min(lambda_n,10**5))
        if _gcd(lambda_n,e) == 1:
            break
    d = _extended_gcd(lambda_n,e)
    p,q,lambda_n=0,0,0
    return (n,e,d)

# Pienin yhteinen monikerta (Least Common Multiple) löytyy näppärästi
# suurimman yhteisen tekijän kautta.

def _lcm(a,b):
    return (a*b)//_gcd(a,b)

# Suurin yhteinen tekijä (Greatest Common Divider) löytyy Eukleideen
# algoritmillä. Etsitään pienemmän numeron mahdollisimman suuri
# monikerta, joka on enintään yhtäsuuri kuin iso numero. Lasketaan
# näiden erotus, asetetaan pienempi numero isomman tilalle ja erotus
# pienemmän. Toistetaan kunnes erotus on 0. Suurin yhteinen tekijä on
# mikä jää "isomman numeron" paikalle.  

def _gcd(a,b):
    bigger = max(a,b)
    smaller = min(a,b)
    while smaller != 0:
        temp = smaller
        smaller = bigger%smaller
        bigger = temp
    return bigger

# Tämä laajennetun suurimman yhteisen tekijän algoritmin versio hakee
# yksityisen avaimen purkueksponentin

def _extended_gcd(a,b):
    (old_r,r)=(a,b)
    (old_t,t)=(0,1)
    while r != 0:
        quotient = _quotient_from_eucleidian_div(old_r, r)
        (old_r,r)=(r,old_r - quotient*r)
        (old_t,t)=(t,old_t - quotient*t)
    return old_t

# Tällä haetaan kahden luvun (kokonainen) osamäärä

def _quotient_from_eucleidian_div(a,b):
    quotient = a//b
    return quotient