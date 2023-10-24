import Funktiot.paikannus as locator
import Funktiot.avaintallennus as keyhandler
import Funktiot.salaus as encrypt

def _decrypt_ui():
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