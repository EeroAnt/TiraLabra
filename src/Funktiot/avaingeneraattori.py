import Funktiot.alkulukugeneraattori as primegenerator
import Funktiot.matikkapalikat as mathaid
import random

# RSA-avain koostuu modulosta (n), salauseksponentista (e) ja
# purkueksponentista (d). n on yksinkertaisesti 2 suuren alkuluvun
# tulo. Ja loput lasketaan alla olevilla funktioilla. p, q ja
# lambda_n nollataan varuilta. Niiden avulla voisi laskea avaimen 
# salaisen osan.

# Haluamme 1024-bittisiä lukuja. Siispä annamme ensimmäiseksi
# parametriksi "_generate_probable_prime" funktiolle 1024. Tämän
# kokoisille alkuluvuille 40 on sopiva määrä "haastamisia"
# useamman lähteen mukaan. Siispä tämä toiseksi parametriksi

# Valitsen e:n väliltä 100, 10000 (kuitenkin pienempi kuin
# lambda_n) kompromissina tehokkuuden ja turvallisuuden välille.
# Tarkempaa infoa toteutusdokumentissa 

def _generate_key():
    p = primegenerator._generate_probable_prime(1024,40)
    q = primegenerator._generate_probable_prime(1024,40)
    while p == q:
        q = primegenerator._generate_probable_prime(1024,40)
    n = p*q
    lambda_n=mathaid._lcm(p-1,q-1)
    e = random.randint(100,min(lambda_n,10**5))
    while mathaid._gcd(lambda_n,e) != 1:
        e = random.randint(100,min(lambda_n,10**5))
    d = mathaid._extended_gcd(lambda_n,e)
    p,q,lambda_n=0,0,0
    return (n,e,d)
