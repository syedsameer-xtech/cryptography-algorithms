def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))

def interactive_demo():
    print("🔐 XOR Cipher Encryption & Decryption 🔐")
    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").strip().lower()
    text = input("Enter the text: ").strip()
    key = input("Enter the secret key: ").strip()

    if not key:
        print("❌ Key cannot be empty.")
        return

    result = xor_encrypt_decrypt(text, key)

    if choice == 'e':
        print(f"\n✅ Encrypted Text (Raw): {result}")
        hex_output = result.encode().hex()
        print(f"✅ Encrypted Text (Hex): {hex_output}")
    elif choice == 'd':
        print(f"\n🔓 Decrypted Text: {result}")
    else:
        print("❌ Invalid option selected.")

if __name__ == "__main__":
    interactive_demo()


# Sample Output
# 🔐 XOR Cipher Encryption & Decryption 🔐
# Type 'e' to Encrypt or 'd' to Decrypt: e
# Enter the text: secret123
# Enter the secret key: key

# ✅ Encrypted Text (Raw): 
# 
# 
# ✅ Encrypted Text (Hex): 021f06180a1903

# 🔐 XOR Cipher Encryption & Decryption 🔐
# Type 'e' to Encrypt or 'd' to Decrypt: d
# Enter the text: 
# 
# Enter the secret key: key

# 🔓 Decrypted Text: secret123
