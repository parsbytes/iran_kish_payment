
# Payment Gateway for Iran Kish

This Python package allows users to easily integrate with the Iran Kish payment gateway for sending payment requests and processing transactions. The package also includes encryption functionality using AES, RSA, and SHA-256 for secure communication with the bank.


## Features

- Sending payment requests to Iran Kish gateway.
- Verifying payment status.
- Encryption using AES, RSA, and SHA-256 for secure communication.


## Installation

Install the package via pip

```bash
  pip install iran_kish_payment
```
Make sure you also have `pycryptodome` installed for encryption:

```bash
  pip install pycryptodome
```
    
## Usage
Sending request to bank
```python
from iran_kish_payment import request_payment

pub_key_pem = """GIVEN PUB KEY FROM BANK"""

BANK_RESPONSE = request_payment(
    terminal_id: "PAYANE", 
    acceptor_id: "PAZIRANDE", 
    password: "PASSWORD", 
    amount: 1000, # IRR
    pub_key_pem: pub_key_pem, 
    request_id: "12334", # length 20
    revert_uri: "https://example.com" # callback url
    )

print(BANK_RESPONSE)

```


## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Author

- [@parsbytes](https://www.github.com/parsbytes)

