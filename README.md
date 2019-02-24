# Paytm-Python-Django (For python 3)
Paytm-Payment Gateway Example On Python-Django

* First clone the project, open your terminal and enter the command

```javascript
git clone https://github.com/itsnikhil/paytm-django.git
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
```
*Staging Credentials
```
PAYTM_MERCHANT_KEY = "<YOUR-PAYTM-STAGING-MERCHANT-KEY>"
PAYTM_MERCHANT_ID = "<YOUR-PAYTM-STAGING-MERCHANT-ID>"
```

*Make Migrations
```
python manage.py makemigrations
```

*Migrate paytm app for transactions details
```
python manage.py migrate paytm
```

*Create Super user
```
python manage.py createsuperuser
```

* Now in terminal run the server and go to http://localhost:8000/
```
python manange.py runserver
```

*Go to
```
1) http://localhost:8000/admin
    - Log in using superuser credentials
2) http://localhost:8000/paytm

This should redirect you to Paytm Page.
Test Credentials to use for login:
Mobile Number – 7777777777
Password – Paytm12345
OTP – 489871

```

### Stuff used to make this:

 * [PAYTM API DOCUMENTATION](http://paywithpaytm.com/developer/paytm_api_doc/)
 * [SDK DOCUMENTATION](http://paywithpaytm.com/developer/paytm_sdk_doc/)
