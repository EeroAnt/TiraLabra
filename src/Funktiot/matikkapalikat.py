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
    while old_t < 0:
        old_t += a
    return old_t

# Tällä haetaan kahden luvun (kokonainen) osamäärä

def _quotient_from_eucleidian_div(a,b):
    quotient = a//b
    return quotient


def _factor_out(number):
    i = 0
    while number%2 == 0:
        i += 1
        number //= 2
    return (i, number)
