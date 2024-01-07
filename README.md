# Auto Coupon

This python project is an example of how we can use gkeepapi to grab a shopping list from google keep and apply coupons based that list.

Current stores supported are:
* Harris Teeters
* Publix
* Target (coming soon)

To run, must use Python version 3.8.18 or 3.8.2

Create a .env file that has the following parameters:
* KEEP_USER="Google Keep Email"
* KEEP_PWD="Google Keep App Password" #(Generate a app password from Google security settings to achieve this.)
* KEEP_LIST="Google Keep ID" #(You can get this from opening the google keep note and seeing the long string in the url)
* SHOP_USERID="Harris Teeter User email"
* SHOP_PWD="Harris Teeter User password"
* PUBLIX_USERID="Publix user name"
* PUBLIX_PWD="Publix password"
* PUBLIX_KEEP_LIST="Google Keep ID"
* TARGET_USERID="Target User email"
* TARGET_PWD="Target password"
* TARGET_KEEP_LIST="Google Keep ID"

Then run
```shell
pip install -r requirements.txt
```

