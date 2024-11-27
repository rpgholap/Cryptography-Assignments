import math

def encrypt_message(msg, key):
    # Remove spaces from the message
    msg = msg.replace(" ", "")
    cipher = ""
    key_len = len(key)
    msg_len = len(msg)
    rows = math.ceil(msg_len / key_len)
    
    # Fill the matrix with characters of the message in row-major order
    matrix = [['' for _ in range(key_len)] for _ in range(rows)]
    k = 0
    for i in range(rows):
        for j in range(key_len):
            if k < msg_len:
                matrix[i][j] = msg[k]
                k += 1
    
    # Sort the columns based on the custom key order
    sorted_key_idx = [int(c) - 1 for c in key]  # Adjust to 0-based index
    
    # Read the columns in sorted order
    for idx in sorted_key_idx:
        for row in range(rows):
            if matrix[row][idx] != '':
                cipher += matrix[row][idx]

    return cipher

def decrypt_message(cipher, key):
    msg = ""
    key_len = len(key)
    cipher_len = len(cipher)
    rows = math.ceil(cipher_len / key_len)

    # Create a matrix to fill column by column based on the sorted key
    matrix = [['' for _ in range(key_len)] for _ in range(rows)]
    
    # Sort the key to get the order of columns
    sorted_key_idx = [int(c) - 1 for c in key]  # Adjust to 0-based index

    # Fill the matrix column by column
    k = 0
    for idx in sorted_key_idx:
        for row in range(rows):
            if k < cipher_len:
                matrix[row][idx] = cipher[k]
                k += 1

    # Read the matrix row by row to reconstruct the message
    for row in matrix:
        msg += ''.join(row)

    return msg

# Example usage with user input
if __name__ == "__main__":
    # Get user input for message and key
    message = input("Enter the message to be encrypted: ")
    key = input("Enter the numeric key (e.g., 431256): ")
    
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted Message: {decrypted_message}")


'''
Enter the message to be encrypted: amhi punekar
Enter the numeric key (e.g., 431256): 2314
Encrypted Message: muahnrapkie
Decrypted Message: amhipunekar

'''