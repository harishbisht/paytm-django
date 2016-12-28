# Paytm-Python-Django
Paytm-Payment Gateway Example On Python-Django

* First clone the project, open your terminal and enter the command

```javascript
git clone https://github.com/harishbisht/paytm-django.git
```
* Now create a virtual environment
```javascript
virtualenv paytm
```
* Now activate the virtual environment
```javascript
source paytm/bin/activate
```
* Now enter into the project folder
```javascript
cd paytm-django/payments/
```
* Now install the requirements 
```javascript
pip install -r requirements.txt
```
* Now go to payments ->settings.py and enter your credentials
```
PAYTM_MERCHANT_KEY=  "<YOUR-PAYTM-MERCHANT-KEY>"
PAYTM_MERCHANT_ID = "<YOUR-PAYTM-MERCHANT-ID>"
PAYTM_CALLBACK_URL = "http://localhost:8000/response/"
```

* Now in terminal run the server and go to http://localhost:8000/
```
python manange.py runserver
```

### Stuff used to make this:

 * [PAYTM API DOCUMENTATION](http://paywithpaytm.com/developer/paytm_api_doc/) 
 * [SDK DOCUMENTATION](http://paywithpaytm.com/developer/paytm_sdk_doc/) 
