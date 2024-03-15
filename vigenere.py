def vigenere_encryption(plaintext, key):
    
    ciphertext = ""
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    plaintext = plaintext.upper()
    
    key = key.upper()

    key_length = len(key)
    
    for i, char in enumerate(plaintext): # Iterating over each character in the plaintext and taking each count with enumerate
        
        if char in alphabet:
           
            char_index = alphabet.find(char)
            
            key_char = key[i % key_length] #Finding the index of the corresponding character in the key

            key_index = alphabet.find(key_char)
            
            new_index = (char_index + key_index) % 26 # Applying encrypt function

            ciphertext += alphabet[new_index]
        else:
            ciphertext += char

    return ciphertext

plaintext = input("Enter Plaintext here:")
key = input("Enter Key for encryption:")
encrypted_text = vigenere_encryption(plaintext, key)
print("Encrypted ciphertext:", encrypted_text)


def vigenere_decryption(ciphertext, key):
    
    decrypted_ciphertext = ""
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ciphertext = ciphertext.upper()
    
    key = key.upper()

    key_length = len(key)
    
    for i, char in enumerate(ciphertext): # Iterating over each character in the ciphertext and taking each count with enumerate
        
        if char in alphabet:
           
            char_index = alphabet.find(char)
            
            key_char = key[i % key_length] #Finding the index of the corresponding character in the key

            key_index = alphabet.find(key_char)
            
            new_index = (26 + char_index - key_index) % 26 # Applying decrypt function

            decrypted_ciphertext += alphabet[new_index]
        else:
            decrypted_ciphertext += char

    return decrypted_ciphertext

ciphertext = input("Enter Ciphertext here:")
key = input("Enter Key for decryption:")
decrypted_text = vigenere_decryption(ciphertext, key)
print("Decrypted ciphertext:", decrypted_text.lower())


bomma

def vigenere_encrypt(plaintext, key):
    
    encrypted_text = ""
    
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    plaintext = plaintext.upper()
    key = key.upper()
    key_length = len(key)
    
    for i, char in enumerate(plaintext):
        
        if char in alphabet:
           
            char_index = alphabet.find(char)
           
            key_char = key[i % key_length]
            key_index = alphabet.find(key_char)
            
            new_index = (char_index + key_index) % 26
            
            encrypted_text += alphabet[new_index]
        else:
            # If the character is not in the alphabet, keep it unchanged
            encrypted_text += char
    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    """
    Decrypts the given ciphertext using Vigenère Cipher with the specified key.
    """
    decrypted_text = ""
    # Define the alphabet
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Convert the ciphertext and key to uppercase for consistency
    ciphertext = ciphertext.upper()
    key = key.upper()
    key_length = len(key)
    # Iterate over each character in the ciphertext
    for i, char in enumerate(ciphertext):
        # Check if the character is in the alphabet
        if char in alphabet:
            # Find the index of the character in the alphabet
            char_index = alphabet.find(char)
            # Find the index of the corresponding character in the key
            key_char = key[i % key_length]
            key_index = alphabet.find(key_char)
            # Apply the reverse shift
            new_index = (char_index - key_index) % 26
            # Append the decrypted character to the result
            decrypted_text += alphabet[new_index]
        else:
            # If the character is not in the alphabet, keep it unchanged
            decrypted_text += char
    return decrypted_text

# Example usage:
plaintext = "HELLO"
key = "KEY"
encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
