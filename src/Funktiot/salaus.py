import Funktiot.avaintallennus as keyhandler

def _encrypt(message,key,name_of_message):
    string_to_bytes = message.encode('utf-8') + b'\x01'
    bytes_to_int = int.from_bytes(string_to_bytes, 'little')
    encrypted_msg = pow(bytes_to_int,int(key[0]),int(key[1]))
    with open("messages/"+name_of_message+".txt", "w") as file:
        file.write(str(encrypted_msg))


def _decrypt(filename,key):
    try:
        with open("messages/"+filename+".txt", "r") as file:
            message = int(file.read())
    except:
        return "Tiedostoa ei löytynyt"
    try:
        bytes_to_recover = pow(message,int(key[0]),int(key[1]))
        recoveredbytes = bytes_to_recover.to_bytes((bytes_to_recover.bit_length()+7)//8, 'little')
        recoveredstring = recoveredbytes[:-1].decode('utf-8')
        return recoveredstring
    except:
        return "Avain ei ollut yhteensopiva"
