

def _save_key(name, public_modulus,public_exponent,private_decryptor):
    public_name = name +"_public"
    private_name = name + "_private"
    keys = []
    keys.append(str(public_exponent)+"\n")
    keys.append(str(public_modulus)+"\n")
    with open("keys/"+public_name, 'w') as file:
        file.writelines(keys)
    with open("keys/"+private_name, 'w') as file:
        file.writelines(str(private_decryptor)+"\n")
        file.writelines(str(public_modulus)+"\n")

def _get_key(key):
    with open("keys/"+key,'r') as file:
        keys = file.readlines()
    return (keys[0],keys[1])