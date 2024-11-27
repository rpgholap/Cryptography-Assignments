import math

def gcd(a, b):
    """Compute the greatest common divisor (GCD) of two numbers."""
    while b:
        a, b = b, a % b
    return a

def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def rsa_key_generation():
    """Generate RSA keys."""
    # Step 1: Choose two distinct prime numbers (p and q)
    while True:
        p = int(input("Enter a small prime number p: "))
        if is_prime(p):
            break
        print("The number is not prime. Please enter a prime number.")
    
    while True:
        q = int(input("Enter another small prime number q (different from p): "))
        if is_prime(q) and p != q:
            break
        print("The number is not prime or is equal to p. Please enter a valid prime number.")
    
    # Step 2: Compute n = p * q and φ(n) = (p-1)*(q-1)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Step 3: Choose an encryption key e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    print(f"Choose a value for e (1 < e < {phi}) such that gcd(e, {phi}) = 1:")
    while True:
        e = int(input("Enter e: "))
        if 1 < e < phi and gcd(e, phi) == 1:
            break
        print("Invalid value for e. Please try again.")
    
    # Step 4: Compute the decryption key d such that (e * d) % φ(n) = 1
    d = pow(e, -1, phi)  # Modular multiplicative inverse
    
    # Public and private keys
    public_key = (e, n)
    private_key = (d, n)
    print(f"\nPublic Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    return public_key, private_key

def rsa_encrypt(message, public_key):
    """Encrypt a message using the public key."""
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher

def rsa_decrypt(cipher, private_key):
    """Decrypt a cipher using the private key."""
    d, n = private_key
    decrypted_message = ''.join([chr((char ** d) % n) for char in cipher])
    return decrypted_message

# Example usage
if __name__ == "__main__":
    print("RSA Key Generation:")
    public_key, private_key = rsa_key_generation()
    
    # Encryption
    message = input("\nEnter the message to encrypt: ")
    cipher = rsa_encrypt(message, public_key)
    print(f"Encrypted Message: {cipher}")
    
    # Decryption
    decrypted_message = rsa_decrypt(cipher, private_key)
    print(f"Decrypted Message: {decrypted_message}")
