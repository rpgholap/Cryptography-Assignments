# Cryptography and Network Security Assignments 🚀

Welcome to the **Cryptography and Network Security** repository! This project contains a collection of 9 implemented cryptographic algorithms as part of my 7th-semester coursework. Each implementation is accompanied by detailed writeups and working code to help you understand the concepts behind the algorithms.

---

## 📋 Table of Contents
- [About the Repository](#about-the-repository)
- [Implemented Algorithms](#implemented-algorithms)
- [Getting Started](#getting-started)
- [Usage Instructions](#usage-instructions)
- [Algorithm Descriptions](#algorithm-descriptions)
- [Learning Outcomes](#learning-outcomes)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

---

## 🌟 About the Repository

This repository showcases fundamental cryptographic algorithms and techniques, implemented in Python, with clear and concise code. It is a blend of classical encryption and modern key exchange methods, aiming to deepen understanding of cryptography's role in securing information.

---

## ✅ Implemented Algorithms

1. **Caesar Cipher**  
2. **Playfair Cipher**  
3. **Polyalphabetic Cipher**  
4. **Hill Cipher**  
5. **Rail Fence Technique**  
6. **Simple Columnar Transposition**  
7. **Advanced Columnar Transposition**  
8. **Diffie-Hellman Key Exchange**  
9. **Simple RSA Algorithm**

---

## 📜 Algorithm Descriptions

### 1. Caesar Cipher
- **Description**: Substitutes each letter by a fixed number of positions.
- **Example**:
  - Input: `HELLO`, Shift: `3`
  - Output: `KHOOR`

### 2. Playfair Cipher
- **Description**: Encrypts digraphs using a 5x5 key matrix. Key used: `LDRP`.
- **Example**:
  - Input: `HELLO`
  - Output: `GDKKN`

### 3. Polyalphabetic Cipher
- **Description**: Uses a series of substitution alphabets for encryption.
- **Example**:
  - Input: `HELLO`, Key: `KEY`
  - Output: `RIJVS`

### 4. Hill Cipher
- **Description**: Encrypts blocks of text using matrix multiplication.
- **Example**:
  - Input: `ACT`, Key: `[[2,3],[1,4]]`
  - Output: `PXQ`

### 5. Rail Fence Technique
- **Description**: Rearranges text using a zigzag pattern.
- **Example**:
  - Input: `HELLO`, Key: `2`
  - Output: `HLOEL`

### 6. Simple Columnar Transposition
- **Description**: Rearranges text based on column ordering.
- **Example**:
  - Input: `HELLO WORLD`, Key: `3142`
  - Output: `HOREL WLLOD`

### 7. Advanced Columnar Transposition
- **Description**: Adds layers of transposition for enhanced security.
- **Example**:
  - Input: `HELLO WORLD`, Key: `3142`, Additional Key: `231`
  - Output: `OELLH DLROW`

### 8. Diffie-Hellman Key Exchange
- **Description**: Securely exchanges keys over an insecure channel.
- **Example**:
  - Input: Public Key: `23`, Base: `5`
  - Output: Shared Key: `19`

### 9. Simple RSA Algorithm
- **Description**: Encrypts and decrypts text using the RSA algorithm.
- **Example**:
  - Input: `HELLO`, Primes: `3, 11`
  - Output: Encrypted: `79`, Decrypted: `HELLO`

---

## 💡 Learning Outcomes

- Understand classical cryptographic techniques.
- Implement modern key exchange algorithms.
- Learn matrix manipulation and modular arithmetic.

---

## 🧰 Technologies Used

- **Programming Language**: Python
- **Libraries**: Standard Python libraries, NumPy (for matrix operations in Hill Cipher)

---

