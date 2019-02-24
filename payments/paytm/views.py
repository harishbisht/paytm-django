from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings

from . import Checksum


from paytm.models import PaytmHistory
# Create your views here.


@login_required
def home(request):
    return HttpResponse("<html><p>Welcome " + request.user.username + "</p><a href='" + settings.HOST_URL + "/paytm/payment'>PayNow</html>")


@login_required
def payment(request):
    user = request.user
    settings.USER = user
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    CALLBACK_URL = settings.HOST_URL + settings.PAYTM_CALLBACK_URL
    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()

    bill_amount = 100
    if bill_amount:
        data_dict = {
            'MID': MERCHANT_ID,
            'ORDER_ID': order_id,
            'TXN_AMOUNT': bill_amount,
            'CUST_ID': user.email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': settings.PAYTM_WEBSITE,
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': CALLBACK_URL,
        }
        param_dict = data_dict
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
        return render(request, "payment.html", {'paytmdict': param_dict, 'user': user})
    return HttpResponse("Bill Amount Could not find. ?bill_amount=10")


@csrf_exempt
def response(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            for key in request.POST:
                if key == "BANKTXNID" or key == "RESPCODE":
                    if request.POST[key]:
                        data_dict[key] = int(request.POST[key])
                    else:
                        data_dict[key] = 0
                elif key == "TXNAMOUNT":
                    data_dict[key] = float(request.POST[key])
            PaytmHistory.objects.create(user=settings.USER, **data_dict)
            return render(request, "response.html", {"paytm": data_dict})
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)
