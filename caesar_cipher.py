def caesar_cipher_encrypt(text, shift):
    """
    Encrypts the given plaintext using Caesar Cipher.
    :param text: Plaintext to encrypt
    :param shift: Number of positions to shift
    :return: Encrypted ciphertext
    """
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result


def caesar_cipher_decrypt(text, shift):
    """
    Decrypts the given ciphertext using Caesar Cipher.
    :param text: Ciphertext to decrypt
    :param shift: Number of positions to reverse shift
    :return: Decrypted plaintext
    """
    return caesar_cipher_encrypt(text, -shift)


# Example usage
if __name__ == "__main__":
    print("Welcome to Caesar Cipher")
    choice = input("Choose: Encrypt (E) or Decrypt (D): ").upper()

    if choice in ['E', 'D']:
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value (key): "))
        if choice == 'E':
            print(f"Ciphertext: {caesar_cipher_encrypt(text, shift)}")
        else:
            print(f"Decrypted Text: {caesar_cipher_decrypt(text, shift)}")
    else:
        print("Invalid choice! Please choose either E or D.")


''' Input and Output :

Welcome to Caesar Cipher
Choose: Encrypt (E) or Decrypt (D): E
Enter the text: junnar
Enter the shift value (key): 3
Ciphertext: mxqqdu

'''