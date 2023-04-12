import socket
import os
from Crypto.Cipher import DES, AES
from Crypto.Random import get_random_bytes

# Constants
BLOCK_SIZE_DES = 8
BLOCK_SIZE_AES = 16
PAD_CHAR = b' '
FILE_PATH = "example.txt"  # Path to the file you want to send
ENCRYPTED_FILE_PATH_DES = "example_encrypted_des.bin"  # Path to store the encrypted file with DES
ENCRYPTED_FILE_PATH_AES = "example_encrypted_aes.bin"  # Path to store the encrypted file with AES
KEY_DES = b'EightByt'  # 64-bit (8-byte) DES encryption key
KEY_AES = get_random_bytes(16)  # 128-bit (16-byte) AES encryption key
HOST = '127.0.0.1'  # Server IP address
PORT = 12345  # Server port

# Pad the data to be a multiple of BLOCK_SIZE
def pad_data(data, block_size):
    return data + (block_size - len(data) % block_size) * PAD_CHAR

# Encrypt the data using DES-ECB mode
def encrypt_data_des(data, key):
    cipher = DES.new(key, DES.MODE_ECB)  # Create a new DES cipher object in ECB mode
    ciphertext = cipher.encrypt(pad_data(data, BLOCK_SIZE_DES))  # Encrypt the data with padding
    return ciphertext

# Encrypt the data using AES-CBC mode
def encrypt_data_aes(data, key):
    iv = get_random_bytes(BLOCK_SIZE_AES)  # Generate a random IV (Initialization Vector)
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Create a new AES cipher object in CBC mode
    ciphertext = cipher.encrypt(pad_data(data, BLOCK_SIZE_AES))  # Encrypt the data with padding
    return iv + ciphertext

# Read the file and encrypt it with DES
with open(FILE_PATH, 'rb') as file:
    file_data = file.read()
    encrypted_data_des = encrypt_data_des(file_data, KEY_DES)

# Write the encrypted data to a new file
with open(ENCRYPTED_FILE_PATH_DES, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data_des)

# Read the file and encrypt it with AES
with open(FILE_PATH, 'rb') as file:
    file_data = file.read()
    encrypted_data_aes = encrypt_data_aes(file_data, KEY_AES)

# Write the encrypted data to a new file
with open(ENCRYPTED_FILE_PATH_AES, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data_aes)

print("Files encrypted successfully and saved as: ")
print("DES: " + ENCRYPTED_FILE_PATH_DES)
print("AES: " + ENCRYPTED_FILE_PATH_AES)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print("Server is ready to receive files...")

while True:
    # Accept a client connection
    client_socket, client_address