# def rail_fence_encryption(plaintext, depth):
    
#     fence = [['' for _ in range(len(plaintext))] for _ in range(depth)] # Creating empty matrix for railfence
#     # Direction variables for moving along the fence
#     down = False
#     row = 0

#     # Fill the rail fence matrix with the plaintext
#     for char in plaintext:
#         # Change direction if we've reached the top or bottom rail
#         if row == 0 or row == depth - 1:
#             down = not down
#         # Add the current character to the rail fence matrix
#         fence[row] += char
#         # Move up or down along the rail fence
#         if down:
#             row += 1
#         else:
#             row -= 1

#     # Concatenate the rows of the fence to create the encrypted text
#     encrypted_text = ''
#     for i in range(depth):
#         encrypted_text += ''.join(fence[i])

#     return encrypted_text

# # Example usage:
# plaintext = "HELLO"
# depth = 3
# encrypted_text = rail_fence_encrypt(plaintext, depth)
# print("Encrypted:", encrypted_text)

#  def railfence_encryption(plaintext, depth):

#     matrix = [['' for cols in range(len(plaintext))] for rows in range(depth)]
#     row = 0
#     col = 0
#     i = 1
#     while col< len(plaintext):
#         if row+i<0 or row+i>=depth:
#             i=i*-1
#         matrix[row][col] = plaintext[col]

#         row+=i
#         col+=1

#     ciphertext = ''
#     for j in matrix:
#         ciphertext+=''.join(j)
#     return ciphertext

# plaintext = input("Enter Plaintext here:")
# depth = input("Enter Depth for encryption:")
# encrypted_text = railfence_encryption(plaintext, depth)
# print("Encrypted ciphertext:", encrypted_text)

def railfence_encryption(plaintext, depth):
    matrix = [['' for cols in range(len(plaintext))] for rows in range(depth)]
    row = 0
    col = 0
    i = 1
    while col < len(plaintext):
        if row + i < 0 or row + i >= depth:
            i = i * -1
        matrix[row][col] = plaintext[col]
        row += i
        col += 1

    ciphertext = ''
    for j in matrix:
        ciphertext += ''.join(j)
    return ciphertext.upper()

plaintext = input("Enter Plaintext here:")
depth = int(input("Enter Depth for encryption:"))
encrypted_text = railfence_encryption(plaintext, depth)
print("Encrypted ciphertext:", encrypted_text)

# def railfence_decryption(ciphertext, depth):
    
#     matrix = [['' for cols in range(len(ciphertext))] for rows in range(depth)]
    
#     row = 0
#     col = 0
#     i = 1
    
#     for char in ciphertext:
#         if row + i < 0 or row + i >= depth:
#             i = i * -1
#         matrix[row][col] = '*'
#         row += i
#         col += 1
    
#     row = 0
#     col = 0
#     i = 1
    
#     for char in ciphertext:
#         if row + i < 0 or row + i >= depth:
#             i = i * -1
#         matrix[row][col] = char
#         row += i
#         col += 1
    
#     row = 0
#     col = 0
#     i = 1
#     plaintext = ''
    
#     for _ in range(len(ciphertext)):
#         if row + i < 0 or row + i >= depth:
#             i = i * -1
#         plaintext += matrix[row][col]
#         row += i
#         col += 1
    
#     return plaintext

# ciphertext = input("Enter Ciphertext here:")
# depth = int(input("Enter Depth for decryption:"))
# decrypted_text = railfence_decryption(ciphertext, depth)
# print("Decrypted plaintext:", decrypted_text)

# def rail_fence_decryption(ciphertext, depth):
#     # Initialize the fence matrix
#     matrix = [['' for _ in range(len(ciphertext))] for _ in range(depth)]
    
#     # Initialize variables
#     row = 0
#     col = 0
#     i = 1
    
#     # Fill the fence matrix with '*' characters to preserve the pattern
#     for _ in range(len(ciphertext)):
#         if row + i < 0 or row + i >= depth:
#             i = i * -1
#         matrix[row][col] = '*'
#         row += i
#         col += 1
    
#     # Reset variables for reading characters from the matrix
#     row = 0
#     col = 0
#     i = 1
#     plaintext = ''
    
#     # Fill the fence matrix with the ciphertext characters
#     for char in ciphertext:
#         if row + i < 0 or row + i >= depth:
#             i = i * -1
#         matrix[row][col] = char
#         row += i
#         col += 1
    
#     # Reset variables for reading characters from the matrix
#     row = 0
#     col = 0
#     i = 1
    
#     # Read characters from the fence matrix to obtain the plaintext
#     for _ in range(len(ciphertext)):
#         if row + i < 0 or row + i >= depth:
#             i = i * -1
#         plaintext += matrix[row][col]
#         matrix[row][col] = '*'  # Reset the matrix cell to '*'
#         row += i
#         col += 1
    
#     return plaintext

# # Example usage:
# ciphertext = input("Enter Ciphertext here: ")
# depth = int(input("Enter Depth for decryption: "))
# decrypted_text = rail_fence_decryption(ciphertext, depth)
# print("Decrypted plaintext:", decrypted_text)


def rail_fence_decryption(ciphertext, depth):
    
    matrix = [['' for _ in range(len(ciphertext))] for _ in range(depth)]
    
    row = 0
    down = False
    
    for i in range(len(ciphertext)):
        matrix[row][i] = '*'
        if row == 0 or row == depth - 1:
            down = not down
        if down:
            row += 1
        else:
            row -= 1
    
    index = 0
    for i in range(depth):
        for j in range(len(ciphertext)):
            if matrix[i][j] == '*' and index < len(ciphertext):
                matrix[i][j] = ciphertext[index]
                index += 1
    
    plaintext = ''
    row = 0
    down = False
    for i in range(len(ciphertext)):
        plaintext += matrix[row][i]
        if row == 0 or row == depth - 1:
            down = not down
        if down:
            row += 1
        else:
            row -= 1
    
    return plaintext

ciphertext = input("Enter Ciphertext here: ")
depth = int(input("Enter Depth for decryption: "))
decrypted_text = rail_fence_decryption(ciphertext, depth)
print("Decrypted plaintext:", decrypted_text)
