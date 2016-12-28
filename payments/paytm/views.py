from django.shortcuts import render
from django.http import HttpResponse
import Checksum
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import random,string
# Create your views here.


def home(request):
    return HttpResponse("<html><a href='http://localhost:8000/payment'>PayNow</html>")


def payment(request):
    MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
    MERCHANT_ID = settings.PAYTM_MERCHANT_ID
    CALLBACK_URL = settings.PAYTM_CALLBACK_URL

    # Generating unique temporary ids
    order_id = Checksum.__id_generator__()

    bill_amount = "100"
    data_dict = {
                'MID':MERCHANT_ID,
                'ORDER_ID':order_id,
                'TXN_AMOUNT': bill_amount,
                'CUST_ID':'harish@pickrr.com',
                'INDUSTRY_TYPE_ID':'Retail',
                'WEBSITE':'WEB_STAGING',
                'CHANNEL_ID':'WEB',
                'CALLBACK_URL':CALLBACK_URL,
            }
    param_dict = data_dict  
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, MERCHANT_KEY)
    return render(request,"payment.html",{'paytmdict':param_dict})

@csrf_exempt
def response(request):
    if request.method == "POST":
        MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
        data_dict = {}
        for key in request.POST:
            data_dict[key] = request.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            return render(request,"response.html",{"paytm":data_dict})
        else:
            return HttpResponse("checksum verify failed")
    return HttpResponse(status=200)