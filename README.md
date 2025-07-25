# 🔐 Cryptographic Algorithms – Mini Projects

This repository contains implementations of fundamental cryptographic algorithms written in Python. It is designed to demonstrate secure encryption and decryption techniques as part of a cybersecurity internship project.

## 📚 Contents

- ✅ Caesar Cipher (`caesar_cipher.py`)
- ✅ XOR Cipher (`xor_cipher.py`)
- ✅ RSA Encryption (`rsa_demo.py`)
- 📂 `output_screenshots/` – Sample output images for each program

---

## 1. Caesar Cipher (🔁 Shift Cipher)

A classical encryption technique that shifts each letter of the plaintext by a fixed number of positions in the alphabet.

### 🔧 Features
- Encrypt and decrypt user input
- Handles both uppercase and lowercase letters
- Ignores non-alphabet characters

### 📦 File: `caesar_cipher.py`
```bash
python caesar_cipher.py

Sample Output

🔐 Advanced Caesar Cipher Demo 🔐
Type 'e' to Encrypt or 'd' to Decrypt: e
Enter the text: hello
Enter the shift amount (e.g. 3): 5

xor_cipher.py
python xor_cipher.py
🖥️ Sample Output

🔐 XOR Cipher Demo 🔐
Enter the message: hello
Enter the key: secret

✅ Encrypted (hex): 1f021f...
🔓 Decrypted Message: hello

✅ Encrypted Text: mjqqt

rsa_demo.py

pip install cryptography
python rsa_demo.py
🖥️ Sample Output

🔐 RSA Encryption & Decryption Demo 🔐
Enter the message to encrypt: hello from Sameer

✅ Encrypted Message (hex): 5a0f...c21 (truncated)
🔓 Decrypted Message: hello from Sameer
