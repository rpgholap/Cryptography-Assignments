def encrypt_rail_fence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    direction_down = False
    row, col = 0, 0

    for char in text:
        rail[row][col] = char
        col += 1

        if row == 0 or row == key - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return "".join(result)


def decrypt_rail_fence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        result.append(rail[row][col])
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1
    
    return "".join(result)


# Get input from user
plaintext = input("Enter the plaintext: ").replace(" ", "")
key = int(input("Enter the key (number of rails): "))

# Encrypt the plaintext
encrypted_text = encrypt_rail_fence(plaintext, key)
print("Encrypted text:", encrypted_text)

# Decrypt the ciphertext
decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Decrypted text:", decrypted_text)


'''
Enter the plaintext: junnar shivneri
Enter the key (number of rails): 3
Encrypted text: jairunrhveinsn
Decrypted text: junnarshivneri

'''