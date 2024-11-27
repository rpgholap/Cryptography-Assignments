def vigenere_encrypt(plaintext, keyword):
    keyword = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]
    
    ciphertext = []
    
    for pt_char, key_char in zip(plaintext, keyword):
    
        if pt_char.isalpha():
            
            shift = ord(key_char.lower()) - ord('a')
            
            if pt_char.islower():
                encrypted_char = chr((ord(pt_char) - ord('a') + shift) % 26 + ord('a'))
            elif pt_char.isupper():
                encrypted_char = chr((ord(pt_char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            # If it's not an alphabetic character, just append it unchanged
            ciphertext.append(pt_char)
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    keyword = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]
    
    plaintext = []
    
    for ct_char, key_char in zip(ciphertext, keyword):
        if ct_char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if ct_char.islower():
                decrypted_char = chr((ord(ct_char) - ord('a') - shift) % 26 + ord('a'))
            elif ct_char.isupper():
                decrypted_char = chr((ord(ct_char) - ord('A') - shift) % 26 + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(ct_char)
    
    return ''.join(plaintext)

if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")
    keyword = input("Enter the keyword: ")
    
    # Encryption
    encrypted = vigenere_encrypt(plaintext, keyword)
    
    # Decryption
    decrypted = vigenere_decrypt(encrypted, keyword)

    print("Plaintext: ", plaintext)
    print("Keyword: ", keyword)
    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)

# Input:
# Enter the plaintext: Hello World
# Enter the keyword: Key

# Output:
# Plaintext:  Hello World
# Keyword:  Key
# Encrypted:  Rijvs Uyvjn
# Decrypted:  Hello World
