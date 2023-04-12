import socket
from Crypto.Cipher import DES, AES

# Constants
BLOCK_SIZE = 8
PAD_CHAR = ' '
ENCRYPTED_FILE_PATH = "example_encrypted.bin"  # Path to store the received encrypted file
DECRYPTED_FILE_PATH = "example_decrypted.txt"  # Path to store the decrypted file
KEY = b'EightByt'  # 64-bit (8-byte) DES encryption key
HOST = '127.0.0.1'  # Server IP address
PORT = 12345  # Server port

# Unpad the data by removing the padding characters
def unpad_data(data):
    return data.rstrip(PAD_CHAR)

# Decrypt the data using DES-ECB mode
def decrypt_data(data, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Create a new DES cipher object in ECB mode
    decrypted_data = cipher.decrypt(data)

# Decrypt the data using AES-CBC mode
def decrypt_data(data, key):
    iv = data[:BLOCK]