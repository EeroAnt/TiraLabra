import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as keyhandler
import Funktiot.salaus as encrypt
import Funktiot.paikannus as locator

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
            try:
                keyhandler._save_key(name, public_modulus,public_exponent,private_decryptor)
                print(f"\nAvain, {name}, tallennettu\n")
            except:
                print("\nJotain meni pieleen\n")
        if choise == "2":
            msg_to_encrypt = input("Salattava viesti: ")
            key_to_use = input("Millä avaimella: ")
            key_type = input("Julkinen vai yksityinen? (j/y)")
            if key_type == "j":
                key = keyhandler._get_key(key_to_use+"_public")
            elif key_type == "y":
                key = keyhandler._get_key(key_to_use+"_private")
            if key != None:
                name_of_message = input("Minkä nimiseen tiedostoon viesti tallennetaan?\nJätä tiedostopäätteet pois ja mielellään myös erikoismerkit varuilta.")
                encrypt._encrypt(msg_to_encrypt, key, name_of_message)
                print("\nSalattu\n")
        if choise =="3":
            file_to_decrypt = input("Minkä nimisen tiedoston viestin salaus puretaan?")
            if locator._locate_message(file_to_decrypt):
                key_to_use = input("Millä avaimella:")
                if locator._locate_key(key_to_use):              
                    key_type = input("Julkinen vai yksityinen? (j/y)")
                    if key_type == "j":
                        key = keyhandler._get_key(key_to_use+"_public")
                    elif key_type == "y":
                        key = keyhandler._get_key(key_to_use+"_private")
                    message = encrypt._decrypt(file_to_decrypt,key)
                    print("\n"+message+"\n")
                else:
                    print("\nAvainta ei löytynyt\n")
            else:
                print("\nTiedostoa ei löytynyt\n")
        if choise == "0":
            break