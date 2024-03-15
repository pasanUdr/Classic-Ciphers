def caesar_encryption(plaintext, key):
    
    ciphertext = ""
   
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    plaintext = plaintext.upper()
    
    for char in plaintext:
        
        if char in alphabet:
            
            char_index = alphabet.find(char) #Finding the index of the character in the alphabet
            
            new_index = (char_index + key) % 26 #Applying the key increment
            
            ciphertext += alphabet[new_index] #Appending the encrypted character to the ciphertext result
        else:
            
            ciphertext += char #If character is not in the alphabet, it won't changed
    return ciphertext

plaintext = input("Enter Plaintext here:")
key = int(input("Enter Key for encryption:"))
encrypted_text = caesar_encryption(plaintext, key)
print("Encrypted ciphertext:", encrypted_text)


def caesar_decryption(ciphertext, key):
    
    decrypted_ciphertext = ""
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ciphertext = ciphertext.upper()
    
    for char in ciphertext:
        
        if char in alphabet:
            
            char_index = alphabet.find(char) #Finds the index of the character in the alphabet
            
            new_index = (char_index - key) % 26 #Applying the key reversing
            
            decrypted_ciphertext += alphabet[new_index] #Appends the decrypted character to the decrypted_ciphertext
        else:
           
            decrypted_ciphertext += char #If character is not in the alphabet, it won't changed
            
    return decrypted_ciphertext

ciphertext = input("Enter Ciphertext here:")
key = int(input("Enter Key for decryption:"))
decrypted_text = caesar_decryption(ciphertext, key)
print("Decrypted plaintext:", decrypted_text.lower())


# # Example usage:
# plaintext = "HELLO"
# shift = 3
# encrypted_text = caesar_encrypt(plaintext, shift)
# print("Encrypted:", encrypted_text)
# decrypted_text = caesar_decrypt(encrypted_text, shift)
# print("Decrypted:", decrypted_text)



# p = input("Enter Plaintext here:")
# k = int(input("Enter Key for encryption:"))

# print(k%5)

bomma

def vigenere_encrypt(plaintext, key):
    
    encrypted_text = ""
    key_index = 0
    for char in plaintext:
        
        shift = ord(key[key_index % len(key)]) - ord('A')

        if 'A' <= char <= 'Z':
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
    
        elif 'a' <= char <= 'z':
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    
    decrypted_text = ""
    key_index = 0
    for char in ciphertext:
        
        shift = ord(key[key_index % len(key)]) - ord('A')

        if 'A' <= char <= 'Z':
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        
        elif 'a' <= char <= 'z':
            decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            decrypted_text += char

    return decrypted_text

plaintext = input("Enter Plaintext here:")
key = int(input("Enter Key for encryption:"))
encrypted_text = caesar_encryption(plaintext, key)
print("Encrypted ciphertext:", encrypted_text)

ciphertext = input("Enter Ciphertext here:")
key = int(input("Enter Key for decryption:"))
decrypted_text = caesar_decryption(ciphertext, key)
print("Decrypted plaintext:", decrypted_text.lower())
