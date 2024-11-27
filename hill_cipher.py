import numpy as np

# Function to generate the key matrix for the key string
def getKeyMatrix(key, n):
    keyMatrix = [[0] * n for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keyMatrix

# Function to encrypt the message
def encrypt(messageVector, keyMatrix, n):
    messageVector = np.array(messageVector)
    keyMatrix = np.array(keyMatrix)
    cipherMatrix = np.dot(keyMatrix, messageVector) % 26
    return cipherMatrix

def HillCipher(message, key):
    # Determine the size of the matrix (n x n)
    n = int(len(key)**0.5)
    
    # Check if key length is a perfect square
    if n * n != len(key):
        print("Error: The key length must be a perfect square (e.g., 4, 9, 16, etc.).")
        return
    
    # Pad the message if it's not a multiple of n
    while len(message) % n != 0:
        message += 'X'

    # Generate the key matrix
    keyMatrix = getKeyMatrix(key, n)

    # Encrypt the message in blocks of size n
    cipherText = []
    for i in range(0, len(message), n):
        messageBlock = [ord(message[j]) % 65 for j in range(i, i + n)]
        cipherBlock = encrypt(messageBlock, keyMatrix, n)
        cipherText.extend([chr(num + 65) for num in cipherBlock])

    # Print the ciphertext
    print("Ciphertext:", "".join(cipherText))    

# Driver Code
def main():
    # Get the message to be encrypted from the user
    message = input("Enter the message: ").upper()

    # Get the key from the user
    key = input("Enter the key (length should be a perfect square): ").upper()

    HillCipher(message, key)

if __name__ == "__main__":
    main()
