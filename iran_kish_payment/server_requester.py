from time import time
import requests


def request_to_server(iv: str, data: str, terminal_id: str, acceptor_id: str, amount: int, request_id: str,
                      revert_uri: str):
    timestamp = int(time())
    # pass the ssl error
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    except AttributeError:
        pass

    try:
        url = 'https://ikc.shaparak.ir/api/v3/tokenization/make'
        json_payload = {
            "authenticationEnvelope": {
                "iv": iv,
                "data": data
            },
            "request": {
                "transactionType": "Purchase",
                "terminalId": terminal_id,
                "acceptorId": acceptor_id,
                "amount": int(amount),
                "revertUri": revert_uri,
                "requestId": request_id,
                "requestTimestamp": timestamp,
            }
        }
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.post(url=url, json=json_payload, headers=headers, verify=False)
        response.raise_for_status()
    except requests.exceptions.ConnectionError as e:
        print('ConnectionError: ', e)
    except requests.exceptions.RequestException as e:
        print('RequestException: ', e)
    except Exception as e:
        print('Exception: ', e)
    else:
        try:
            return response.json()
        except ValueError:
            print('Response content is not in JSON format:', response.text)
