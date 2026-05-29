import os
from cryptography.fernet import Fernet

def generate_key():
    """Generates a key and saves it into a file"""
    key = Fernet.generate_key()
    return key

def encrypt_file(file_path, key):
    """Encrypts a file"""
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)
    tabs_path = os.path.join(base_path, "tabs")
    
    # Generate a key
    key = generate_key()
    
    print("\n" + "="*50)
    print("IMPORTANT: Copy the encryption key below and save it to .streamlit/secrets.toml")
    print("ENCRYPTION_KEY = \"" + key.decode() + "\"")
    print("="*50 + "\n")
    
    # Encrypt ch1.md ~ ch6.md
    for i in range(1, 7):
        file_name = f"ch{i}.md"
        file_path = os.path.join(tabs_path, file_name)
        if os.path.exists(file_path):
            encrypt_file(file_path, key)
            print(f"[OK] {file_name} encrypted -> {file_name}.enc")
        else:
            print(f"[FAIL] {file_name} not found.")
    
    print("\nDone. Check the tabs folder for .enc files.")
