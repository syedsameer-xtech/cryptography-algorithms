from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64
import os
import sys

# ================= CONSTANTS =================

KEY_SIZE = 2048
PUBLIC_EXPONENT = 65537
MAX_MESSAGE_SIZE = (KEY_SIZE // 8) - 2 * 32 - 2  # OAEP padding overhead

# ================= KEY MANAGEMENT =================

def generate_keys(key_size: int = KEY_SIZE) -> tuple:
    """Generate RSA key pair."""
    private_key = rsa.generate_private_key(
        public_exponent=PUBLIC_EXPONENT,
        key_size=key_size,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def save_keys(private_key, public_key, private_path: str = "private_key.pem", 
              public_path: str = "public_key.pem") -> None:
    """Save keys to PEM files."""
    # Save private key (encrypted with password)
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b"changeme123")  # ⚠️ Change this!
    )
    with open(private_path, "wb") as f:
        f.write(private_pem)
    
    # Save public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(public_path, "wb") as f:
        f.write(public_pem)
    
    print(f"✅ Keys saved: {private_path}, {public_path}")

def load_keys(private_path: str = "private_key.pem", 
              public_path: str = "public_key.pem") -> tuple:
    """Load keys from PEM files."""
    # Load public key
    with open(public_path, "rb") as f:
        public_key = serialization.load_pem_public_key(f.read(), backend=default_backend())
    
    # Load private key (with password)
    with open(private_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=b"changeme123",  # ⚠️ Must match save password
            backend=default_backend()
        )
    
    return private_key, public_key

# ================= ENCRYPTION / DECRYPTION =================

def encrypt_message(public_key, message: str) -> bytes:
    """Encrypt message using RSA-OAEP with SHA256."""
    if len(message.encode()) > MAX_MESSAGE_SIZE:
        raise ValueError(f"Message too long! Max {MAX_MESSAGE_SIZE} bytes for {KEY_SIZE}-bit key.")
    
    return public_key.encrypt(
        message.encode("utf-8"),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def decrypt_message(private_key, encrypted_data: bytes) -> str:
    """Decrypt RSA-OAEP ciphertext."""
    return private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    ).decode("utf-8")

def format_output(data: bytes, format_type: str = "base64") -> str:
    """Format binary data for display."""
    if format_type == "base64":
        return base64.b64encode(data).decode("ascii")
    elif format_type == "hex":
        return data.hex()
    return str(data)

def parse_input(data: str, format_type: str = "base64") -> bytes:
    """Parse formatted string back to bytes."""
    if format_type == "base64":
        return base64.b64decode(data.strip())
    elif format_type == "hex":
        return bytes.fromhex(data.strip())
    return data.encode()

# ================= INTERACTIVE DEMO =================

def print_banner():
    """Print application banner."""
    print("\n" + "🔐" * 25)
    print("   RSA Encryption & Decryption Tool")
    print("🔐" * 25 + "\n")

def get_choice(prompt: str, options: list) -> str:
    """Get validated user choice."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"❌ Please enter one of: {', '.join(options)}")

def interactive_demo():
    """Main interactive menu."""
    print_banner()
    
    private_key = None
    public_key = None
    
    while True:
        print("\n📋 Main Menu:")
        print("  [1] Generate new key pair")
        print("  [2] Load keys from files")
        print("  [3] Encrypt a message")
        print("  [4] Decrypt a message")
        print("  [5] Quick demo (generate + encrypt + decrypt)")
        print("  [q] Quit")
        
        choice = get_choice("\nSelect option (1-5/q): ", ['1', '2', '3', '4', '5', 'q'])
        
        if choice == 'q':
            print("\n👋 Goodbye! Stay secure. 🔐\n")
            break
        
        if choice == '1':
            try:
                key_size = int(input("Enter key size (2048/4096) [default: 2048]: ").strip() or "2048")
                if key_size not in [2048, 4096]:
                    print("⚠️ Using default 2048-bit key.")
                    key_size = 2048
                
                print("🔄 Generating keys (this may take a moment)...")
                private_key, public_key = generate_keys(key_size)
                
                if input("💾 Save keys to files? (y/n): ").strip().lower() == 'y':
                    save_keys(private_key, public_key)
                
                print("✅ Keys generated successfully!")
                
            except Exception as e:
                print(f"❌ Error generating keys: {e}")
        
        elif choice == '2':
            try:
                private_path = input("Private key file [private_key.pem]: ").strip() or "private_key.pem"
                public_path = input("Public key file [public_key.pem]: ").strip() or "public_key.pem"
                
                if not os.path.exists(private_path) or not os.path.exists(public_path):
                    print("❌ One or both key files not found!")
                    continue
                
                private_key, public_key = load_keys(private_path, public_path)
                print("✅ Keys loaded successfully!")
                
            except Exception as e:
                print(f"❌ Error loading keys: {e}")
                print("💡 Make sure the password matches when saving/loading keys.")
        
        elif choice == '3':
            if not public_key:
                print("⚠️ Please generate or load keys first (option 1 or 2).")
                continue
            
            try:
                message = input("Enter message to encrypt: ").strip()
                if not message:
                    print("❌ Message cannot be empty.")
                    continue
                
                encrypted = encrypt_message(public_key, message)
                
                # Show in preferred format
                fmt = get_choice("Show output as [base64/hex]: ", ['base64', 'hex'])
                print(f"\n✅ Encrypted ({fmt.upper()}):")
                print(format_output(encrypted, fmt))
                
                # Optional: Copy to clipboard hint
                print("\n💡 Tip: Save this encrypted text to decrypt later!")
                
            except ValueError as e:
                print(f"❌ {e}")
            except Exception as e:
                print(f"❌ Encryption error: {e}")
        
        elif choice == '4':
            if not private_key:
                print("⚠️ Please generate or load keys first (option 1 or 2).")
                continue
            
            try:
                fmt = get_choice("Encrypted input format [base64/hex]: ", ['base64', 'hex'])
                encrypted_input = input(f"Enter {fmt.upper()} encrypted data: ").strip()
                
                if not encrypted_input:
                    print("❌ Input cannot be empty.")
                    continue
                
                encrypted_bytes = parse_input(encrypted_input, fmt)
                decrypted = decrypt_message(private_key, encrypted_bytes)
                
                print(f"\n🔓 Decrypted Message: {decrypted}")
                
            except Exception as e:
                print(f"❌ Decryption error: {e}")
                print("💡 Ensure you're using the correct private key and input format.")
        
        elif choice == '5':
            # Quick end-to-end demo
            print("\n🔄 Running quick demo...")
            try:
                priv, pub = generate_keys()
                message = input("Enter a short message: ").strip() or "Hello from RSA!"
                
                encrypted = encrypt_message(pub, message)
                decrypted = decrypt_message(priv, encrypted)
                
                print(f"\n📝 Original:  {message}")
                print(f"🔐 Encrypted: {format_output(encrypted)[:64]}... (truncated)")
                print(f"🔓 Decrypted: {decrypted}")
                print(f"✅ Match: {message == decrypted}")
                
            except Exception as e:
                print(f"❌ Demo failed: {e}")

# ================= COMMAND LINE MODE =================

def quick_encrypt(public_key_pem: str, message: str) -> str:
    """One-liner encryption for scripting."""
    from cryptography.hazmat.primitives import serialization
    public_key = serialization.load_pem_public_key(
        public_key_pem.encode(), backend=default_backend()
    )
    encrypted = encrypt_message(public_key, message)
    return format_output(encrypted)

def quick_decrypt(private_key_pem: str, encrypted_b64: str) -> str:
    """One-liner decryption for scripting."""
    from cryptography.hazmat.primitives import serialization
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(), password=b"changeme123", backend=default_backend()
    )
    encrypted_bytes = parse_input(encrypted_b64)
    return decrypt_message(private_key, encrypted_bytes)

# ================= MAIN =================

if __name__ == "__main__":
    # Check for required package
    try:
        from cryptography.hazmat.primitives.asymmetric import rsa
    except ImportError:
        print("❌ Missing required package: cryptography")
        print("📦 Install with: pip install cryptography")
        sys.exit(1)
    
    # Run interactive demo
    interactive_demo()
