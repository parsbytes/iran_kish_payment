from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import hashlib


def encrypt_aes(data: str):
    binary_data = bytes.fromhex(data)
    key = get_random_bytes(16)  # 128-bit key
    iv = get_random_bytes(16)
    padded_data = pad(binary_data, AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_data)
    return key.hex(), iv.hex(), ciphertext
