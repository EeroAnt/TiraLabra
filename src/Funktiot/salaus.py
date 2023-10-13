import Funktiot.avaintallennus as keyhandler

def _encrypt(message,public_key):
    # keyhandler._get_key()
    string_to_bytes = message.encode('utf-8') + b'\x01'
    bytes_to_int = int.from_bytes(string_to_bytes, 'little')
    encrypted_msg = pow(bytes_to_int,int(public_key[0]),int(public_key[1]))
    name_of_message = input("Minkä nimiseen tiedostoon viesti tallennetaan?\nJätä tiedostopäätteet pois ja mielellään myös erikoismerkit varuilta  ")
    with open("messages/"+name_of_message+".txt", "w") as file:
        file.write(str(encrypted_msg))


def _decrypt(filename,private_key):
    try:
        with open("messages/"+filename+".txt", "r") as file:
            message = int(file.read())
    except:
        print("Tiedostoa ei löytynyt")
        return
    try:
        bytes_to_recover = pow(message,int(private_key[0]),int(private_key[1]))
        recoveredbytes = bytes_to_recover.to_bytes((bytes_to_recover.bit_length()+7)//8, 'little')
        recoveredstring = recoveredbytes[:-1].decode('utf-8')
        print(recoveredstring)
    except:
        print("Avain ei ollut yhteensopiva")
