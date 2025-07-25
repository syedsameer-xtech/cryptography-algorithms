from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message(public_key, message):
    return public_key.encrypt(
        message.encode(),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

def decrypt_message(private_key, encrypted_message):
    return private_key.decrypt(
        encrypted_message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    ).decode()

def interactive_demo():
    print("🔐 RSA Encryption & Decryption Demo 🔐")
    private_key, public_key = generate_keys()

    message = input("Enter the message to encrypt: ")

    encrypted = encrypt_message(public_key, message)
    print("\n✅ Encrypted Message (in hex):", encrypted.hex())

    decrypted = decrypt_message(private_key, encrypted)
    print("🔓 Decrypted Message:", decrypted)

if __name__ == "__main__":
    interactive_demo()


# Sample Output
# 🔐 RSA Encryption & Decryption Demo 🔐
# Enter the message to encrypt: hello from Sameer

# ✅ Encrypted Message (in hex): 3f71a4...d82 (truncated for brevity)
# 🔓 Decrypted Message: hello from Sameer
