from iran_kish_payment.aes_encryptor import encrypt_aes
from iran_kish_payment.b_str_generator import generate_b_str
from iran_kish_payment.server_requester import request_to_server
from iran_kish_payment.rsa_encryptor import encrypt_rsa
from iran_kish_payment.sha256_hasher import sha256_hash


def request_payment(terminal_id: str, acceptor_id: str, password: str, amount: int, pub_key_pem: str, request_id: str,
                    revert_uri: str):
    b_str = generate_b_str(terminal_id=terminal_id, password=password, amount=amount)
    key, iv, ciphertext = encrypt_aes(b_str)
    hashed_data = sha256_hash(ciphertext)
    str_to_rsa = key + hashed_data
    encrypted_data = encrypt_rsa(data=str_to_rsa, pub_key_pem=pub_key_pem)

    res = request_to_server(terminal_id=terminal_id, acceptor_id=acceptor_id, amount=amount, iv=iv,
                            data=encrypted_data, request_id=request_id, revert_uri=revert_uri)
    # print(res)
    return res
