import Funktiot.avaintallennus as keyhandler

def _encrypt(message,public_key):
    # keyhandler._get_key()
    string_to_bytes = message.encode('utf-8') + b'\x01'
    bytes_to_int = int.from_bytes(string_to_bytes, 'little')
    with open("messages/testo","w") as file:
        file.write(str(bytes_to_int))
    encrypted_msg = pow(bytes_to_int,int(public_key[0]),int(public_key[1]))
    name_of_message = input("Minkä nimiseen tiedostoon viesti tallennetaan?\nJätä tiedostopäätteet pois ja mielellään myös erikoismerkit varuilta  ")
    with open("messages/"+name_of_message+".txt", "w") as file:
        file.write(str(encrypted_msg))


def _decrypt(filename,private_key):
    with open("messages/"+filename+".txt", "r") as file:
        message = int(file.read())
    print(message)
    bytes_to_recover = pow(message,int(private_key[0]),int(private_key[1]))
    print(bytes_to_recover)
    recoveredbytes = bytes_to_recover.to_bytes((bytes_to_recover.bit_length()+7)//8, 'little')
    recoveredstring = recoveredbytes[:-1].decode('utf-8')
    print(recoveredstring)

def testing(mystring):
    mybytes = mystring.encode('utf-8') + b'\x01'  # Pad with 1 to preserve trailing zeroes
    myint = int.from_bytes(mybytes, 'little')
    print(myint)
    public = keyhandler._get_key("Koli_public")
    enctypted_message = pow(myint,int(public[0]),int(public[1]))
    private = keyhandler._get_key("Koli_private")
    decrypted_message = pow(enctypted_message,int(private[0]),int(private[1]))
    recoveredbytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, 'little')
    recoveredstring = recoveredbytes[:-1].decode('utf-8') # Strip pad before decoding
    print(recoveredstring)