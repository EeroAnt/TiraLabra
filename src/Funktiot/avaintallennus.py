

def _save_key(name, public_modulus,public_exponent,private_decryptor):
    public_name = name +"_public"
    private_name = name + "_private"
    with open("keys/"+public_name, 'w') as file:
        file.write(str(public_exponent))
        file.write("/n")
        file.write(str(public_modulus))
    with open("keys/"+private_name, 'w') as file:
        file.write(str(private_decryptor))