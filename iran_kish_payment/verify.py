import requests

from get_token import IRAN_KISH


def payment_verify(request):
    """
    This is a simple Django view which which is associated with the call_back_url.
    Just get the logic behind it!
    :param request:
    """
    if request.POST.get('resultCode') == '100':
        request_id = request.POST.get('InvoiceNumber')
        # do what you need to do before verification here

        payload = {
            'merchantId': request.POST.get('merchantId'),
            'referenceId': request.POST.get('referenceId'),
            'token': request.POST.get('token')
        }
        r = requests.post(IRAN_KISH['confirmation_url'], json=payload, verify=False)
        if r.ok:
            result = r.json()
            if result['status']:
                # transaction verification successful
                # do the necessary stuffs ...
                # redirect to a proper endpoint ...
                pass

            else:
                # transaction verification fail
                # do the necessary stuffs ...
                # redirect to a proper endpoint ...
                pass

    # transaction failed
    # do the necessary stuffs ...
    # redirect to a proper endpoint ...

    # you can also check the other result codes for more specific details. (read the ipg docs)
