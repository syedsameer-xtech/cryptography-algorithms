import base64
import hashlib
import os
import sys

# ================= CONSTANTS =================

MIN_KEY_LENGTH = 1
MAX_KEY_LENGTH = 256

# ================= CORE FUNCTIONS =================

def xor_encrypt_decrypt(data: str, key: str) -> str:
    """
    XOR encrypt/decrypt data with key.
    XOR is symmetric - same function works for both operations.
    """
    if not key:
        raise ValueError("Key cannot be empty!")
    
    result = []
    for i, char in enumerate(data):
        key_char = key[i % len(key)]
        xor_result = ord(char) ^ ord(key_char)
        result.append(chr(xor_result))
    
    return ''.join(result)

def encrypt_to_hex(data: str, key: str) -> str:
    """Encrypt and return as hex string (safe for display/storage)."""
    encrypted = xor_encrypt_decrypt(data, key)
    return encrypted.encode('latin-1').hex()

def decrypt_from_hex(hex_data: str, key: str) -> str:
    """Decrypt from hex string back to original text."""
    try:
        encrypted_bytes = bytes.fromhex(hex_data)
        encrypted_str = encrypted_bytes.decode('latin-1')
        return xor_encrypt_decrypt(encrypted_str, key)
    except ValueError as e:
        raise ValueError(f"Invalid hex format: {e}")

def encrypt_to_base64(data: str, key: str) -> str:
    """Encrypt and return as Base64 string (safe for display/storage)."""
    encrypted = xor_encrypt_decrypt(data, key)
    return base64.b64encode(encrypted.encode('latin-1')).decode('ascii')

def decrypt_from_base64(b64_data: str, key: str) -> str:
    """Decrypt from Base64 string back to original text."""
    try:
        encrypted_bytes = base64.b64decode(b64_data)
        encrypted_str = encrypted_bytes.decode('latin-1')
        return xor_encrypt_decrypt(encrypted_str, key)
    except Exception as e:
        raise ValueError(f"Invalid Base64 format: {e}")

def strengthen_key(key: str, salt: str = "xor_salt_v1") -> str:
    """
    Strengthen weak keys using SHA256 hash.
    Makes short keys more secure against brute force.
    """
    combined = f"{key}{salt}"
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    return hashed[:32]  # Use first 32 chars of hash

# ================= FILE OPERATIONS =================

def save_to_file(content: str, filename: str = "encrypted_output.txt") -> bool:
    """Save encrypted content to file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Saved to: {filename}")
        return True
    except Exception as e:
        print(f"❌ Save failed: {e}")
        return False

def load_from_file(filename: str = "encrypted_output.txt") -> str:
    """Load encrypted content from file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {filename}")
    except Exception as e:
        raise Exception(f"❌ Load failed: {e}")

# ================= VALIDATION =================

def validate_key(key: str) -> tuple[bool, str]:
    """Validate key meets requirements."""
    if not key:
        return False, "Key cannot be empty!"
    if len(key) < MIN_KEY_LENGTH:
        return False, f"Key must be at least {MIN_KEY_LENGTH} character!"
    if len(key) > MAX_KEY_LENGTH:
        return False, f"Key must be at most {MAX_KEY_LENGTH} characters!"
    return True, "Valid key"

def validate_hex(hex_string: str) -> tuple[bool, str]:
    """Validate hex string format."""
    try:
        bytes.fromhex(hex_string)
        return True, "Valid hex"
    except ValueError:
        return False, "Invalid hex format (must be even length, 0-9, a-f)"

def validate_base64(b64_string: str) -> tuple[bool, str]:
    """Validate Base64 string format."""
    try:
        base64.b64decode(b64_string)
        return True, "Valid Base64"
    except Exception:
        return False, "Invalid Base64 format"

# ================= INTERACTIVE DEMO =================

def print_banner():
    """Print application banner."""
    print("\n" + "🔐" * 30)
    print("        XOR Cipher Encryption Tool")
    print("🔐" * 30 + "\n")
    print("⚠️  WARNING: XOR is NOT secure for sensitive data!")
    print("   Use for learning, CTFs, or non-critical data only.\n")

def get_choice(prompt: str, options: list) -> str:
    """Get validated user choice."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"❌ Please enter one of: {', '.join(options)}")

def get_key() -> str:
    """Get and validate encryption key."""
    while True:
        key = input("Enter secret key: ").strip()
        valid, msg = validate_key(key)
        if valid:
            # Offer key strengthening
            if len(key) < 8:
                strengthen = input("⚠️ Short key detected. Strengthen with hash? (y/n): ").strip().lower()
                if strengthen == 'y':
                    key = strengthen_key(key)
                    print(f"✅ Key strengthened (now {len(key)} chars)")
            return key
        print(f"❌ {msg}")

def interactive_demo():
    """Main interactive menu."""
    print_banner()
    
    while True:
        print("\n📋 Main Menu:")
        print("  [1] Encrypt text (output as Hex)")
        print("  [2] Encrypt text (output as Base64)")
        print("  [3] Decrypt from Hex")
        print("  [4] Decrypt from Base64")
        print("  [5] Load from file & decrypt")
        print("  [6] Quick test (encrypt + decrypt)")
        print("  [h] Show security info")
        print("  [q] Quit")
        
        choice = get_choice("\nSelect option (1-6/h/q): ", 
                           ['1', '2', '3', '4', '5', '6', 'h', 'q'])
        
        if choice == 'q':
            print("\n👋 Goodbye! Stay secure. 🔐\n")
            break
        
        elif choice == 'h':
            print_security_info()
            continue
        
        elif choice == '6':
            # Quick end-to-end test
            print("\n🔄 Running quick test...")
            try:
                text = input("Enter test message: ").strip() or "XOR test message"
                key = get_key()
                
                encrypted_hex = encrypt_to_hex(text, key)
                decrypted = decrypt_from_hex(encrypted_hex, key)
                
                print(f"\n📝 Original:  {text}")
                print(f"🔐 Encrypted: {encrypted_hex[:64]}..." if len(encrypted_hex) > 64 else f"🔐 Encrypted: {encrypted_hex}")
                print(f"🔓 Decrypted: {decrypted}")
                print(f"✅ Match: {text == decrypted}")
                
            except Exception as e:
                print(f"❌ Test failed: {e}")
            continue
        
        # Get key for encryption/decryption operations
        key = get_key()
        
        if choice in ['1', '2']:
            # Encrypt
            try:
                text = input("Enter text to encrypt: ").strip()
                if not text:
                    print("❌ Text cannot be empty.")
                    continue
                
                if choice == '1':
                    result = encrypt_to_hex(text, key)
                    fmt = "HEX"
                else:
                    result = encrypt_to_base64(text, key)
                    fmt = "BASE64"
                
                print(f"\n✅ Encrypted ({fmt}):")
                print(result)
                
                # Optional: Save to file
                if input("\n💾 Save to file? (y/n): ").strip().lower() == 'y':
                    filename = input("Enter filename [encrypted_output.txt]: ").strip() or "encrypted_output.txt"
                    save_to_file(result, filename)
                
            except Exception as e:
                print(f"❌ Encryption error: {e}")
        
        elif choice in ['3', '4']:
            # Decrypt
            try:
                if input("📁 Load from file? (y/n): ").strip().lower() == 'y':
                    filename = input("Enter filename [encrypted_output.txt]: ").strip() or "encrypted_output.txt"
                    encrypted_input = load_from_file(filename)
                    print(f"📄 Loaded from {filename}")
                else:
                    fmt = "HEX" if choice == '3' else "BASE64"
                    encrypted_input = input(f"Enter {fmt} encrypted data: ").strip()
                
                if not encrypted_input:
                    print("❌ Input cannot be empty.")
                    continue
                
                # Validate input format
                if choice == '3':
                    valid, msg = validate_hex(encrypted_input)
                    if not valid:
                        print(f"❌ {msg}")
                        continue
                    decrypted = decrypt_from_hex(encrypted_input, key)
                else:
                    valid, msg = validate_base64(encrypted_input)
                    if not valid:
                        print(f"❌ {msg}")
                        continue
                    decrypted = decrypt_from_base64(encrypted_input, key)
                
                print(f"\n🔓 Decrypted Message: {decrypted}")
                
            except FileNotFoundError as e:
                print(f"❌ {e}")
            except Exception as e:
                print(f"❌ Decryption error: {e}")
                print("💡 Ensure you're using the same key and correct format!")
        
        elif choice == '5':
            # Load from file & decrypt
            try:
                filename = input("Enter filename [encrypted_output.txt]: ").strip() or "encrypted_output.txt"
                encrypted_input = load_from_file(filename)
                print(f"📄 Loaded from {filename}")
                
                # Auto-detect format
                if all(c in '0123456789abcdefABCDEF' for c in encrypted_input):
                    print("🔍 Detected: HEX format")
                    decrypted = decrypt_from_hex(encrypted_input, key)
                else:
                    print("🔍 Detected: BASE64 format")
                    decrypted = decrypt_from_base64(encrypted_input, key)
                
                print(f"\n🔓 Decrypted Message: {decrypted}")
                
            except Exception as e:
                print(f"❌ {e}")

def print_security_info():
    """Display security warnings and best practices."""
    print("\n" + "⚠️" * 30)
    print("           SECURITY INFORMATION")
    print("⚠️" * 30)
    print("""
🔴 XOR Cipher Limitations:
   • NOT secure for sensitive data
   • Vulnerable to known-plaintext attacks
   • Key reuse compromises security
   • No authentication/integrity check

✅ When to Use:
   • Learning cryptography concepts
   • CTF challenges
   • Obfuscation (not encryption)
   • Non-critical data

❌ When NOT to Use:
   • Passwords
   • Financial data
   • Personal information
   • Production systems

🔐 Better Alternatives:
   • AES-256 (symmetric)
   • RSA (asymmetric)
   • ChaCha20 (modern symmetric)

📚 Key Best Practices:
   • Use long, random keys (16+ chars)
   • Never reuse keys
   • Combine with hashing for integrity
   • Use established libraries for real security
""")
    print("⚠️" * 30 + "\n")

# ================= MAIN =================

if __name__ == "__main__":
    try:
        interactive_demo()
    except KeyboardInterrupt:
        print("\n\n⚠️ Interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
