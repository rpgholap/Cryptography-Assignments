P = int(input("Enter a prime number (P): "))
G = int(input("Enter a base (G): "))

print(f"Publicly Shared Prime Number (P): {P}")
print(f"Publicly Shared Base (G): {G}")

private_key_alice = int(input("Alice, enter your private key: "))
print(f"Alice's Private Key: {private_key_alice}")

public_key_alice = (G ** private_key_alice) % P
print(f"Alice's Public Key: {public_key_alice}")

private_key_bob = int(input("Bob, enter your private key: "))
print(f"Bob's Private Key: {private_key_bob}")

public_key_bob = (G ** private_key_bob) % P
print(f"Bob's Public Key: {public_key_bob}")

# Step 4: Exchange Public Keys
# Alice and Bob share their public keys with each other

# Step 5: Calculate Shared Secret
# Alice calculates shared secret using Bob's public key
shared_secret_alice = (public_key_bob ** private_key_alice) % P
print(f"Alice's Calculated Shared Secret: {shared_secret_alice}")

# Bob calculates shared secret using Alice's public key
shared_secret_bob = (public_key_alice ** private_key_bob) % P
print(f"Bob's Calculated Shared Secret: {shared_secret_bob}")

# Verifying that the shared secrets are identical
if shared_secret_alice == shared_secret_bob:
    print("\nKey Exchange Successful! Shared Secret Key Established.")
else:
    print("\nKey Exchange Failed! Shared Secrets Do Not Match.")
