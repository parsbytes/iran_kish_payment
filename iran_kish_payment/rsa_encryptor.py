import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt_rsa(data, pub_key_pem):
    public_key = RSA.import_key(pub_key_pem)
    cipher = PKCS1_OAEP.new(public_key)
    message_bytes = binascii.unhexlify(data)
    ciphertext = cipher.encrypt(message_bytes)
    ciphertext_hex = binascii.hexlify(ciphertext)
    return ciphertext_hex.decode()
