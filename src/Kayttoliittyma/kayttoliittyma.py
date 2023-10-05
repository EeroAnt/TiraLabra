import Funktiot.alkulukugeneraattori as primegenerator
import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as save

def UI():
    while True:
        print("Mitä tehdään?")
        options = {1 : "Tuota n-bittinen alkuluku",
                   2 : "Tuota avainpari",
                   0 : "Lopeta"}
        for key, value in options.items():
            print(key, ":", value)
        choise = int(input())
        if choise == 1:
            bits = int(input("Montako bittiä? "))
            attempts = int(input("Monta kertaa haastetaan? "))
            print(primegenerator._generate_probable_prime(bits,attempts))
        if choise == 2:
            (public_modulus, public_exponent, private_decryptor) = keygenerator._generate_key()
            print(f"Julkinen avain ({public_modulus}, {public_exponent}) ja yksityinen avain {private_decryptor}")
            name = input("Millä nimellä avain tallennetaan? ")
            save._save_key(name, public_modulus,public_exponent,private_decryptor)
        if choise == 0:
            break