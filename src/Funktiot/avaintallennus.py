

def _save_key(name, public_modulus,public_exponent,private_decryptor):
    public_name = name +"_public"
    private_name = name + "_private"
    keys = []
    keys.append(str(public_exponent)+"\n")
    keys.append(str(public_modulus)+"\n")
    with open("src/Avaimet/"+public_name, 'w') as file:
        file.writelines(keys)
    with open("src/Avaimet/"+private_name, 'w') as file:
        file.writelines(str(private_decryptor)+"\n")
        file.writelines(str(public_modulus)+"\n")

def _get_key(key):
    try:
        with open("src/Avaimet/"+key,'r') as file:
            keys = file.readlines()
        return (keys[0],keys[1])
    except:
        return None