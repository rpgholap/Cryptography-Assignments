import math

def create_matrix(msg, key_len, fill_char="X"):
    
    rows = math.ceil(len(msg) / key_len)
    padded_msg = msg.ljust(rows * key_len, fill_char)
    matrix = [list(padded_msg[i:i + key_len]) for i in range(0, len(padded_msg), key_len)]
    return matrix

def encrypt_message(msg, key, fill_char="X"):
   
    msg = msg.replace(" ", "")
    
    key_len = len(key)
    matrix = create_matrix(msg, key_len, fill_char)
    
    sorted_key_idx = sorted(range(len(key)), key=lambda x: key[x])
    
    cipher = ""
    for idx in sorted_key_idx:
        for row in matrix:
            cipher += row[idx]
    
    return cipher

def decrypt_message(cipher, key, fill_char="X"):
   
    key_len = len(key)
    cipher_len = len(cipher)
    rows = math.ceil(cipher_len / key_len)
    
    matrix = [['' for _ in range(key_len)] for _ in range(rows)]
    sorted_key_idx = sorted(range(len(key)), key=lambda x: key[x])
    
    k = 0
    for idx in sorted_key_idx:
        for row in range(rows):
            if k < cipher_len:
                matrix[row][idx] = cipher[k]
                k += 1
    
    msg = ""
    for row in matrix:
        msg += ''.join(row)
    
    return msg.rstrip(fill_char)

def advanced_encryption(msg, key, rounds=1):
    
    encrypted_message = msg
    for _ in range(rounds):
        encrypted_message = encrypt_message(encrypted_message, key)
    return encrypted_message

def advanced_decryption(cipher, key, rounds=1):
    
    decrypted_message = cipher
    for _ in range(rounds):
        decrypted_message = decrypt_message(decrypted_message, key)
    return decrypted_message
if __name__ == "__main__":
    message = input("Enter the message to be encrypted: ")
    key = input("Enter the key (alphanumeric allowed): ")
    rounds = int(input("Enter the number of rounds you want to perform: "))
    
    encrypted_message = advanced_encryption(message, key, rounds)
    print(f"Encrypted Message after {rounds} rounds: {encrypted_message}")
    
    decrypted_message = advanced_decryption(encrypted_message, key, rounds)
    print(f"Decrypted Message after {rounds} rounds: {decrypted_message}")


'''
Enter the message to be encrypted: I am a marathon runner
Enter the key (alphanumeric allowed): player
Enter the number of rounds you want to perform: 3
Encrypted Message after 3 rounds: rnnraIuarntehaaomm
Decrypted Message after 3 rounds: Iamamarathonrunner
'''