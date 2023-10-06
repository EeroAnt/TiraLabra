import Funktiot.alkulukugeneraattori as primegenerator
import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as keyhandler
import Funktiot.salaus as encrypt

def UI():
    while True:
        print("Mitä tehdään?")
        options = {1 : "Tuota n-bittinen alkuluku",
                   2 : "Tuota avainpari",
                   3 : "Salaa viesti",
                   4 : "Pura viesti",
                   0 : "Lopeta"}
        for key, value in options.items():
            print(key, ":", value)
        choise = input()
        if choise == "1":
            bits = int(input("Montako bittiä? "))
            attempts = int(input("Monta kertaa haastetaan? "))
            print(primegenerator._generate_probable_prime(bits,attempts))
        if choise == "2":
            (public_modulus, public_exponent, private_decryptor) = keygenerator._generate_key()
            print(f"Julkinen avain ({public_modulus}, {public_exponent}) ja yksityinen avain {private_decryptor}")
            name = input("Millä nimellä avain tallennetaan? ")
            keyhandler._save_key(name, public_modulus,public_exponent,private_decryptor)
        if choise == "3":
            msg_to_encrypt = input("Salattava viesti: ")
            key_to_use = input("Millä avaimella: ")
            public_key = keyhandler._get_key(key_to_use+"_public")
            encrypt._encrypt(msg_to_encrypt, public_key)
        if choise =="4":
            file_to_decrypt = input("Minkä nimisen tiedoston viestin salaus puretaan? ")
            key_to_use = input("Millä avaimella: ")
            private_key = keyhandler._get_key(key_to_use+"_public")
            encrypt._decrypt(file_to_decrypt,private_key)
        if choise =="5":
            string =input()
            encrypt.testing(string)
        if choise == "0":
            break