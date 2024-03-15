def columnar_encryption(plaintext, key):
    
    plaintext = plaintext.replace(" ", "") #Removing spaces in plaintext
    
    ciphertext = ""

    columns = [''] * len(key) #Creating columns based on the key
    for i, char in enumerate(plaintext):
        columns[i % len(key)] += char

    sorted_columns = [col for _, col in sorted(zip(key, columns))] #Rearranging columns based on order of the key

    ciphertext = ''.join(sorted_columns)
    return ciphertext

plaintext = input("Enter Plaintext here: ").upper()
key = input("Enter Key here: ").upper()
encrypted_text = columnar_encryption(plaintext, key)
print("Encrypted ciphertext:", encrypted_text)

def columnar_decryption(ciphertext, key):
    
    num_rows = len(ciphertext) // len(key)
    
    plaintext = ""

    
    columns = [''] * len(key) #Create columns based on the key order
    for i, char in enumerate(ciphertext):
        columns[i // num_rows] += char

    key_order = sorted(range(len(key)), key=lambda k: key[k]) #Rearrange columns based on the key order
    for i in range(num_rows):
        for index in key_order:
            plaintext += columns[index][i]

    return plaintext.lower()

plaintext = input("Enter Ciphertext here: ").upper()
key = input("Enter Key here: ").upper()
decrypted_text = columnar_decryption(encrypted_text, key)
print("Decrypted plaintext:", decrypted_text)


bomma

def columnar_encryption(plaintext, key):

    plaintext = plaintext.replace(" ", "")
    
    ciphertext = ""

    columns = [''] * len(key)
    for i, char in enumerate(plaintext):
        columns[i % len(key)] += char

    sorted_columns = [col for _, col in sorted(zip(key, columns))]

    ciphertext = ''.join(sorted_columns)
    return ciphertext

def columnar_decryption(ciphertext, key):
    
    num_rows = len(ciphertext) // len(key)
    
    plaintext = ""

    columns = [''] * len(key)
    for i, char in enumerate(ciphertext):
        columns[i // num_rows] += char

    key_order = sorted(range(len(key)), key=lambda k: key[k])
    for i in range(num_rows):
        for index in key_order:
            plaintext += columns[index][i]

    return plaintext

plaintext = input("Enter Plaintext here: ").upper()
key = input("Enter Key here: ").upper()

encrypted_text = columnar_encryption(plaintext, key)
print("Encrypted ciphertext:", encrypted_text)

decrypted_text = columnar_decryption(encrypted_text, key)
print("Decrypted plaintext:", decrypted_text)