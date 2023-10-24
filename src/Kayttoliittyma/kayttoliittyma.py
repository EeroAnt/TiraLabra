import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as keyhandler
import Kayttoliittyma.salauskayttoliittyma as encrypt_ui
import Kayttoliittyma.purkkukayttoliittyma as decrypt_ui

def UI():
    while True:
        print("Mitä tehdään?\n")
        options = {1 : "Tuota avainpari",
                   2 : "Salaa viesti",
                   3 : "Pura viesti",
                   0 : "Lopeta"}
        for key, value in options.items():
            print(key, ":", value)
        choise = input()
        if choise == "1":
            (public_modulus, public_exponent, private_decryptor) = keygenerator._generate_key()
            name = input("\nMillä nimellä avain tallennetaan? ")
            keyhandler._save_key(name, public_modulus,public_exponent,private_decryptor)
        if choise == "2":
            encrypt_ui._encrypt_ui()
        if choise =="3":
            decrypt_ui._decrypt_ui()
        if choise == "0":
            break