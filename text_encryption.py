from cryptography.fernet import Fernet
import argparse


# Createing a key for encryption and saves it to a separate file
def generate_key():
    key = Fernet.generate_key()
    with open("secrete_key","wb") as key_file:
        key_file.write(key)
    print("Key generated successfully and saved to a 'secrete_key' file.")

# Grab the generated key

def load_key():
    with open("secrete_key","rb") as key_file:
        key = key_file.read()
        return key

# Encrpyting the text

def encrypt_text(text: str) -> bytes:
    key = load_key()
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text: bytes) -> str:
    key = load_key()
    f=Fernet(key)
    decrypted_text = f.decrypt(encrypted_text).decode()
    return decrypted_text

def main():
    parser = argparse.ArgumentParser(description="Text encryption and decryption using cryptography")
    parser.add_argument("--generate-key", action="store_true",help="Create and key of encryption")
    parser.add_argument("--encrypt", type=str,help="Encryptes the provided text")
    parser.add_argument("--decrypt", type=str,help="Decryptes the provided text")

    args = parser.parse_args()

    if args.generate_key:
        generate_key()
    elif args.encrypt:
        encrypted_text= encrypt_text(args.encrypt)
        print(f"Encrypted text: {encrypted_text.decode()}")
    elif args.decrypt:
        decrypted_text = decrypt_text(args.decrypt.encode())
        print(f"Decrypted text: {decrypted_text}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()