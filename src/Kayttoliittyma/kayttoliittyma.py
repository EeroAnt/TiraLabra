import Funktiot.alkulukugeneraattori as primegenerator
import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as keyhandler
import Funktiot.salaus as encrypt

def UI():
    while True:
        print("Mitä tehdään?")
        options = {1 : "Tuota avainpari",
                   2 : "Salaa viesti",
                   3 : "Pura viesti",
                   0 : "Lopeta"}
        for key, value in options.items():
            print(key, ":", value)
        choise = input()
        if choise == "1":
            (public_modulus, public_exponent, private_decryptor) = keygenerator._generate_key()
            name = input("Millä nimellä avain tallennetaan? ")
            try:
                keyhandler._save_key(name, public_modulus,public_exponent,private_decryptor)
                print(f"Avain, {name}, tallennettu")
            except:
                print("Jotain meni pieleen")
        if choise == "2":
            msg_to_encrypt = input("Salattava viesti: ")
            key_to_use = input("Millä avaimella: ")
            public_key = keyhandler._get_key(key_to_use+"_public")
            name_of_message = input("Minkä nimiseen tiedostoon viesti tallennetaan?\nJätä tiedostopäätteet pois ja mielellään myös erikoismerkit varuilta  ")
            if public_key != None:
                encrypt._encrypt(msg_to_encrypt, public_key, name_of_message)
                print("Salattu")
        if choise =="3":
            file_to_decrypt = input("Minkä nimisen tiedoston viestin salaus puretaan? ")
            key_to_use = input("Millä avaimella: ")
            private_key = keyhandler._get_key(key_to_use+"_private")
            if private_key != None:
                message = encrypt._decrypt(file_to_decrypt,private_key)
                print(message)
        if choise == "0":
            break