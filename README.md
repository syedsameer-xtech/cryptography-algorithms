# 🔐 Cryptography Toolkit

<div align="center">

### Three Essential Encryption Tools for Learning & Practice  

**Caesar Cipher • XOR Cipher • RSA Encryption**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Security](https://img.shields.io/badge/Purpose-Educational-orange.svg)](#)

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Tools Included](#-tools-included)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Detailed Documentation](#-detailed-documentation)
- [Security Comparison](#-security-comparison)
- [Sample Outputs](#-sample-outputs)
- [Testing](#-testing)
- [Security Warnings](#-security-warnings)
- [When to Use Each Tool](#-when-to-use-each-tool)
- [Contributing](#-contributing)
- [License](#-license)
- [Credits](#-credits)

---

## 🎯 Overview

The **Cryptography Toolkit** contains three encryption tools designed for:

✅ Learning cryptography fundamentals  
✅ Practicing CTF challenges  
✅ Educational demonstrations  
✅ Understanding symmetric & asymmetric encryption  

| Tool | Type | Security Level | Best For |
|------|------|----------------|----------|
| **Caesar Cipher** | Classical | 🔴 Very Low | Learning, history |
| **XOR Cipher** | Symmetric | 🟡 Low-Medium | CTFs, obfuscation |
| **RSA** | Asymmetric | 🟢 High | Real encryption, key exchange |

---

## 🛠️ Tools Included

### 🔄 1. Caesar Cipher (`caesar_cipher.py`)

A classic substitution cipher shifting letters by a fixed number.

**Features:**
- Encrypt & decrypt with custom shift
- Brute-force all 26 possibilities
- Preserves case and punctuation
- Interactive CLI menu

**Best For:** Understanding basic cipher mechanics

---

### ⚡ 2. XOR Cipher (`xor_cipher.py`)

A symmetric cipher using the XOR operation with a repeating key.

**Features:**
- Encrypt/decrypt (same function)
- Hex & Base64 outputs
- File load/save support
- Key strengthening option
- Auto-format detection

**Best For:** CTF challenges & learning symmetric encryption

---

### 🔑 3. RSA Encryption (`rsa_tool.py`)

Modern asymmetric encryption using public/private key pairs.

**Features:**
- Generate 2048/4096-bit key pairs
- Save/load password-protected PEM files
- OAEP padding with SHA-256
- Base64 & Hex output formats
- Secure file-based key handling

**Best For:** Real encryption & understanding PKI

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/crypto-toolkit.git
cd crypto-toolkit
```

### 2️⃣ Install Dependencies

```bash
# Required only for RSA tool
pip install -r requirements.txt
```

### 3️⃣ Verify Installation

```bash
python3 caesar_cipher.py
python3 xor_cipher.py
python3 rsa_tool.py
```

---

## 🚀 Quick Start

### Caesar Cipher

```bash
python3 caesar_cipher.py
# Choose: e → Enter text → Enter shift
```

---

### XOR Cipher

```bash
python3 xor_cipher.py
# Choose: 1 → Enter key → Enter text
```

---

### RSA Encryption

```bash
python3 rsa_tool.py
# 1 → Generate keys
# 3 → Encrypt
# 4 → Decrypt
```

---

## 📖 Detailed Documentation

### 🔄 Caesar Cipher Menu

| Command | Description |
|----------|------------|
| e | Encrypt text |
| d | Decrypt with known shift |
| b | Brute-force all shifts |
| q | Quit |

Example:

```
Text: Hello World
Shift: 3
Output: Khoor Zruog
```

---

### 🔑 RSA Tool Menu

| Option | Description |
|--------|------------|
| 1 | Generate new key pair |
| 2 | Load keys |
| 3 | Encrypt message |
| 4 | Decrypt message |
| 5 | Quick demo |
| q | Quit |

---

### ⚡ XOR Cipher Menu

| Option | Description |
|--------|------------|
| 1 | Encrypt (Hex) |
| 2 | Encrypt (Base64) |
| 3 | Decrypt (Hex) |
| 4 | Decrypt (Base64) |
| 5 | Load from file |
| 6 | Quick test |
| h | Security info |
| q | Quit |

---

## 🔒 Security Comparison

| Feature | Caesar | XOR | RSA |
|----------|--------|-----|-----|
| Type | Substitution | Symmetric | Asymmetric |
| Key Size | 1–25 | Variable | 2048–4096 bits |
| Security | 🔴 None | 🟡 Low | 🟢 High |
| Speed | ⚡ Very Fast | ⚡ Fast | 🐌 Slower |
| Production Ready | ❌ No | ❌ No | ✅ Yes |
| Learning Value | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## 📊 Sample Outputs

### Caesar Cipher

```
Encrypted: Lipps, Asvph!
```

### RSA

```
Original: Hello from RSA!
Encrypted: kR3mN8vL2pQ9xYzT...
Decrypted: Hello from RSA!
Match: True
```

### XOR

```
Encrypted: 1a0f2b3c4d5e...
Decrypted: Confidential message
Match: True
```

---

## 🧪 Testing

Run tests individually:

```bash
python3 tests/test_caesar.py
python3 tests/test_rsa.py
python3 tests/test_xor.py
```

Expected Output:

```
All tests passed!
```

---

## ⚠️ Security Warnings

### 🔴 Caesar Cipher
- NOT secure
- Easily broken
- Only 26 keys

### 🟡 XOR Cipher
- Not secure for sensitive data
- Vulnerable to known-plaintext attacks
- Key reuse breaks security

### 🟢 RSA
- Secure if used properly
- Use minimum 2048-bit keys
- Protect private keys carefully

---

## 📚 When to Use Each Tool

| Scenario | Recommended Tool |
|----------|------------------|
| Learning basics | Caesar → XOR → RSA |
| CTF challenges | XOR / Caesar |
| Secure communication | RSA |
| Password storage | ❌ Use bcrypt/argon2 instead |
| Production systems | RSA (proper libraries) |

---

## 🤝 Contributing

Contributions are welcome!

```bash
git checkout -b feature/your-feature
git commit -m "✨ Add feature"
git push origin feature/your-feature
```

**Standards:**
- Python 3.8+
- Type hints required
- Docstrings required
- PEP 8 compliant

---

## 📄 License

MIT License — Free for educational and personal use.

Copyright (c) 2024 Syed Sameer

---

## 🙏 Credits

Developer: **Syed Sameer**  
Libraries: `cryptography`, Python Standard Library  
Inspiration: Cryptography textbooks & CTF challenges  

Made with ❤️ by ChatGPT & Qwen  
Prompted by Syed Sameer  

---

<div align="center">

⭐ Star this repository if you found it useful!  
🔝 Back to Top  

</div>
