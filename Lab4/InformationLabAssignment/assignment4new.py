import time
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import hashlib
import os

def save_key(key, filename):
    with open(filename, 'wb') as file:
        file.write(key)


def load_key(filename):
    with open(filename, 'rb') as file:
        return file.read()


def save_data(data, filename):
    with open(filename, 'wb') as file:
        file.write(data)


def load_data(filename):
    with open(filename, 'rb') as file:
        return file.read()

def aes_encrypt_ECB(mode, key_length, text, key_file, data_file):
    key = get_random_bytes(key_length // 8)
    save_key(key, key_file)
    cipher = AES.new(key, mode)
    padded_text = pad(text, AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    save_data(ciphertext, data_file)
    return ciphertext, cipher


def aes_decrypt_ECB(ciphertext_file, key_file, mode):
    key = load_key(key_file)
    ciphertext = load_data(ciphertext_file)
    cipher = AES.new(key, mode)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext

def aes_encrypt_CFB(mode, key_length, text, key_file, data_file):
    key = get_random_bytes(key_length // 8)
    save_key(key, key_file)
    cipher = AES.new(key, mode)
    iv = cipher.iv
    padded_text = pad(text, AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    save_data(ciphertext, data_file)
    decrypt_cipher = AES.new(key, mode, iv=iv)
    padded_plaintext = decrypt_cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return ciphertext, cipher, plaintext

def rsa_encrypt(text, public_key_file, private_key_file, data_file):
    key = RSA.generate(2048)
    public_key = key.publickey()
    save_key(public_key.export_key(), public_key_file)
    save_key(key.export_key(), private_key_file)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_rsa.encrypt(text)
    save_data(ciphertext, data_file)
    return ciphertext, key


def rsa_decrypt(ciphertext_file, private_key_file):
    private_key = RSA.import_key(load_key(private_key_file))
    ciphertext = load_data(ciphertext_file)
    cipher_rsa = PKCS1_OAEP.new(private_key)
    plaintext = cipher_rsa.decrypt(ciphertext)
    return plaintext

def rsa_sign(text, private_key_file, signature_file):
    key = RSA.import_key(load_key(private_key_file))
    h = SHA256.new(text)
    signature = pkcs1_15.new(key).sign(h)
    save_data(signature, signature_file)
    return signature, key, h


def rsa_verify(signature_file, public_key_file, text):
    public_key = RSA.import_key(load_key(public_key_file))
    signature = load_data(signature_file)
    h = SHA256.new(text)
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("The signature is valid.")
    except (ValueError, TypeError):
        print("The signature is not valid.")

def sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text)
    return sha256.hexdigest()


def main():
    while True:
        print("Choose an option:")
        print("1. AES Encryption/Decryption")
        print("2. RSA Encryption/Decryption")
        print("3. RSA Signature")
        print("4. SHA-256 Hashing")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Choose a mode:")
            print("1. ECB")
            print("2. CFB")
            c = input("Enter your choice: ")

            if c == '1':
                mode = AES.MODE_ECB
                key_length = int(input("Enter key length: "))
                text = load_data("story.txt")
                key_file = 'aes_key.bin'
                data_file = 'aes_encrypted.bin'
                start_time = time.time()
                ciphertext, cipher = aes_encrypt_ECB(mode, key_length, text, key_file, data_file)
                print(f"Ciphertext: {ciphertext}")
                plaintext = aes_decrypt_ECB(data_file, key_file, mode)
                print(f"Plaintext: {plaintext}")
                print(f"Execution Time: {time.time() - start_time} seconds")

            if c == '2':
                mode = AES.MODE_CFB
                key_length = int(input("Enter key length: "))
                text = load_data("story.txt")
                key_file = 'aes_key.bin1'
                data_file = 'aes_encrypted.bin1'
                start_time = time.time()
                ciphertext, cipher, plaintext = aes_encrypt_CFB(mode, key_length, text, key_file, data_file)
                print(f"Ciphertext: {ciphertext}")
                print(f"Plaintext: {plaintext}")
                print(f"Execution Time: {time.time() - start_time} seconds")

        elif choice == '2':
            text = b"Yesterday is history,tomorrow is a mystery,and today is a gift...that's why they call it present"
            public_key_file = 'rsa_public_key.pem'
            private_key_file = 'rsa_private_key.pem'
            data_file = 'rsa_encrypted.bin'
            start_time = time.time()
            ciphertext, key = rsa_encrypt(text, public_key_file, private_key_file, data_file)
            print(f"Ciphertext: {ciphertext}")
            plaintext = rsa_decrypt(data_file, private_key_file)
            print(f"Plaintext: {plaintext}")
            print(f"Execution Time: {time.time() - start_time} seconds")

        elif choice == '3':
            text = b"Life itself is the most wonderful fairy tale."
            private_key_file = 'rsa_private_key.pem'
            public_key_file = 'rsa_public_key.pem'
            signature_file = 'rsa_signature.bin'
            start_time = time.time()
            signature, key, h = rsa_sign(text, private_key_file, signature_file)
            print(f"Signature: {signature}")
            rsa_verify(signature_file, public_key_file, text)
            print(f"Execution Time: {time.time() - start_time} seconds")

        elif choice == '4':
            text = b"Your message here"
            start_time = time.time()
            hash_value = sha256_hash(text)
            print(f"SHA-256 Hash: {hash_value}")
            print(f"Execution Time: {time.time() - start_time} seconds")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()