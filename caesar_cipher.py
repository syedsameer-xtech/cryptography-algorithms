import string

def caesar_encrypt(text: str, shift: int) -> str:
    """ Encrypt text using Caesar cipher with given shift."""
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt Caesar cipher by reversing the shift."""
    return caesar_encrypt(ciphertext, -shift)

def brute_force_decrypt(ciphertext: str) -> None:
    """Try all 26 possible shifts and display results."""
    print("\n🔍 Brute Force Decryption (All 26 Shifts):")
    print("-" * 50)
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f"Shift {shift:2d}: {decrypted}")
    print("-" * 50)

def get_valid_shift() -> int:
    """Prompt user for a valid integer shift value."""
    while True:
        try:
            shift = int(input("Enter shift amount (0-25): ").strip())
            if 0 <= shift <= 25:
                return shift
            print("⚠️ Shift must be between 0 and 25.")
        except ValueError:
            print("❌ Please enter a valid integer.")

def interactive_demo():
    """Main interactive menu for the Caesar cipher tool."""
    print("\n" + "=" * 50)
    print("🔐 Advanced Caesar Cipher Tool 🔐")
    print("=" * 50)
    
    while True:
        print("\n📋 Menu:")
        print("  [e] Encrypt text")
        print("  [d] Decrypt with known shift")
        print("  [b] Brute force decrypt (try all shifts)")
        print("  [q] Quit")
        
        choice = input("\nSelect option (e/d/b/q): ").strip().lower()
        
        if choice == 'q':
            print("\n👋 Goodbye! Stay secure. 🔐")
            break
        
        if choice not in ['e', 'd', 'b']:
            print("❌ Invalid option. Please try again.")
            continue
        
        text = input("Enter text: ").strip()
        if not text:
            print("⚠️ Text cannot be empty.")
            continue
        
        if choice == 'b':
            brute_force_decrypt(text)
            continue
        
        shift = get_valid_shift()
        
        if choice == 'e':
            result = caesar_encrypt(text, shift)
            print(f"\n✅ Encrypted: {result}")
        elif choice == 'd':
            result = caesar_decrypt(text, shift)
            print(f"\n🔓 Decrypted: {result}")
        
        # Optional: Show reverse operation
        if input("\n🔁 Show reverse operation? (y/n): ").strip().lower() == 'y':
            if choice == 'e':
                print(f"   Decrypting back: {caesar_decrypt(result, shift)}")
            else:
                print(f"   Encrypting back: {caesar_encrypt(result, shift)}")

if __name__ == "__main__":
    interactive_demo()
