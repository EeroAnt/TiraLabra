import Funktiot.paikannus as locator
import Funktiot.salaus as encrypt
import Funktiot.avaintallennus as keyhandler

def _encrypt_ui():
    msg_to_encrypt = input("Salattava viesti: ")
    key_to_use = input("Millä avaimella: ")
    if locator._locate_key(key_to_use):
        while True:
            key_type = input("Julkinen vai yksityinen? (j/y)")
            if key_type == "j":
                key = keyhandler._get_key(key_to_use+"_public")
                print()
                break
            elif key_type == "y":
                key = keyhandler._get_key(key_to_use+"_private")
                break
        name_of_message = input("Minkä nimiseen tiedostoon viesti tallennetaan?\nJätä tiedostopäätteet pois ja mielellään myös erikoismerkit varuilta.")
        encrypt._encrypt(msg_to_encrypt, key, name_of_message)
    else:
        print("\nAvainta ei löytynyt\n")
        