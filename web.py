import base64
import codecs
import random
import string
import getpass

# Simple user database (username: password)
users = {
    "admin": "admin123",
    "user1": "pass1"
}

def login():
    print("=== Login ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

def encode_text():
    text = input("Enter text to encode: ")
    print("Choose encoding:")
    print("1. Base64")
    print("2. ROT13")
    choice = input("> ")

    if choice == "1":
        encoded = base64.b64encode(text.encode()).decode()
    elif choice == "2":
        encoded = codecs.encode(text, 'rot_13')
    else:
        print("Invalid choice")
        return
    print("Encoded result:", encoded)

def decode_text():
    text = input("Enter text to decode: ")
    print("Choose decoding:")
    print("1. Base64")
    print("2. ROT13")
    choice = input("> ")

    if choice == "1":
        try:
            decoded = base64.b64decode(text).decode()
        except Exception:
            print("Invalid Base64 input!")
            return
    elif choice == "2":
        decoded = codecs.decode(text, 'rot_13')
    else:
        print("Invalid choice")
        return
    print("Decoded result:", decoded)

def generate_password():
    length = int(input("Password length (8-32): "))
    if length < 8 or length > 32:
        print("Length must be between 8 and 32.")
        return
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)

def main():
    if not login():
        return

    while True:
        print("\n=== Menu ===")
        print("1. Encode text")
        print("2. Decode text")
        print("3. Generate password")
        print("4. Exit")
        choice = input("> ")

        if choice == "1":
            encode_text()
        elif choice == "2":
            decode_text()
        elif choice == "3":
            generate_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
