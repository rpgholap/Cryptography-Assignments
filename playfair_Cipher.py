import string


def generate_playfair_key(key):
    """
    Generates the Playfair cipher key matrix.
    :param key: Input keyword
    :return: 5x5 Playfair matrix
    """
    alphabet = string.ascii_uppercase.replace("J", "")
    key = "".join(dict.fromkeys(key.upper().replace("J", "I") + alphabet))
    return [key[i:i + 5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    """
    Finds the position of a character in the Playfair matrix.
    :param matrix: Playfair matrix
    :param char: Character to find
    :return: (row, col) position of the character
    """
    for row, line in enumerate(matrix):
        if char in line:
            return row, line.index(char)


def playfair_encrypt_pair(matrix, a, b):
    """
    Encrypts a pair of characters using Playfair Cipher rules.
    :param matrix: Playfair key matrix
    :param a: First character
    :param b: Second character
    :return: Encrypted pair
    """
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)

    # Same row
    if row_a == row_b:
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    # Same column
    elif col_a == col_b:
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    # Rectangle
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]


def playfair_encrypt(text, key):
    matrix = generate_playfair_key(key)
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"

    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        if a == b:
            b = "X"
        ciphertext += playfair_encrypt_pair(matrix, a, b)
    return ciphertext

if __name__ == "__main__":
    key = "LDRP"
    plaintext = input("Enter plaintext: ")
    ciphertext = playfair_encrypt(plaintext, key)
    print(f"Encrypted Text: {ciphertext}")


'''
Input and output:

Enter plaintext: hello Junnar 
Encrypted Text: KBRVQHZUUGER

'''