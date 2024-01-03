# Harris Teeters Auto Coupon

This python project is an example of how we can use gkeepapi to grab a shopping list from google keep and apply coupons based that list.

To run, must use Python version 3.8.18

Create a .env file that has the following parameters:
KEEP_USER=<Google Keep Email>
KEEP_PWD=<Google Keep Password>
KEEP_LIST=<Google Keep ID> (You can get this from opening the google keep note and seeing the long string in the url)
SHOP_USERID=<Harris Teeter User email>
SHOP_PWD=<Harris Teeter User password>

Then run
```shell
pip install -r requirements.txt
```

