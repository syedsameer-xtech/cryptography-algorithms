import string

def caesar_encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def interactive_demo():
    print("🔐 Advanced Caesar Cipher Demo 🔐")
    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").strip().lower()
    text = input("Enter the text: ").strip()
    while True:
        try:
            shift = int(input("Enter the shift amount (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a valid integer for shift.")

    if choice == 'e':
        encrypted = caesar_encrypt(text, shift)
        print(f"\n✅ Encrypted Text: {encrypted}")
    elif choice == 'd':
        decrypted = caesar_decrypt(text, shift)
        print(f"\n🔓 Decrypted Text: {decrypted}")
    else:
        print("❌ Invalid option selected.")

if __name__ == "__main__":
    interactive_demo()


# Example Output (When you run it):
# pgsql
# Copy
# Edit
# 🔐 Advanced Caesar Cipher Demo 🔐
# Type 'e' to Encrypt or 'd' to Decrypt: e
# Enter the text: Hello, World!
# Enter the shift amount (e.g. 3): 4

# ✅ Encrypted Text: Lipps, Asvph!
