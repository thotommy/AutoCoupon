from selenium import webdriver
import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
import gkeepapi
from dotenv import load_dotenv
import os
from selenium.webdriver.common.keys import Keys
# Needs to use python version 3.8.18

# Constants
HARRIS_TEETER = "harris teeter"
PUBLIX = "publix"
TARGET = "target"

def get_list(grocery):
    load_dotenv()
    user = os.getenv('KEEP_USER')
    pwd = os.getenv('KEEP_PWD')
    keep = gkeepapi.Keep()
    success = keep.login(user, pwd)

    if(success == True):
        if grocery is HARRIS_TEETER:
            print("Grabbing Harris Teeter list..")
            gnotes = keep.get(os.getenv('KEEP_LIST'))
        elif grocery is PUBLIX:
            print("Grabbing Publix list..")
            gnotes = keep.get(os.getenv('PUBLIX_KEEP_LIST'))
        elif grocery is TARGET:
            print("Grabbing Target list..")
            gnotes = keep.get(os.getenv('TARGET_KEEP_LIST'))
        else:
            print("Grabbing default list..")
            gnotes = keep.get(os.getenv('KEEP_LIST'))

        return f'{gnotes.title} \n\n{gnotes.text}'


def login_harris_teeters(driver):
    print("Login in to Harris Teeter..")
    load_dotenv()
    username = os.getenv('SHOP_USERID')
    pw = os.getenv('SHOP_PWD')
    driver.get("https://www.harristeeter.com")
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[6]/div/div/div/div[6]/div/div/div/button").click() # Click sign in
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[6]/div/div/div/div[6]/div/div/div/div/div/div/ul/li[1]/button").click()
    sleep(3)
    sleep(2)
    driver.find_element(By.XPATH, "//input[@name=\"email\"]").send_keys(username)
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name=\"password\"]").send_keys(pw)
    sleep(3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/main/section/section/section/form/button").click() # Login
    sleep(5)


def apply_harris_teeter_coupons(driver, list_arr):
    print("Applying Harris Teeter Coupons..")
    driver.get("https://www.harristeeter.com/coupons/")
    sleep(5)
    for item in list_arr:
        if '==' in item:
            continue
        print(f'Finding coupons for {item}')
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/main/section/div/section/section/section/div/div[1]/div/div[2]/div[1]/div/input").clear()
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[1]/main/section/div/section/section/section/div/div[1]/div/div[2]/div[1]/div/input").send_keys(item)
        sleep(4)
        clip_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Clip')]")
        if(len(clip_buttons) == 0):
            continue
        for clip_button in clip_buttons:
            clip_button.click()


def login_publix(driver):
    print("Login in to Publix..")
    load_dotenv()
    username = os.getenv('SHOP_USERID')
    pw = os.getenv('SHOP_PWD')
    driver.get("https://www.publix.com/")
    sleep(3)
    driver.find_element(By.XPATH, "//*[@id=\"userLogIn\"]").click()
    sleep(5)
    driver.find_element(By.XPATH, "//input[@name=\"Email address\"]").send_keys(username)
    sleep(2)
    driver.find_element(By.XPATH, "//input[@name=\"Password\"]").send_keys(pw)
    sleep(1)
    driver.find_element(By.XPATH, "//button[@id=\"next\"]").click()
    sleep(10)


def apply_publix_coupons(driver, list_arr):
    print("Applying Publix coupons..")
    driver.get("https://www.publix.com/savings/digital-coupons?nav=header")
    sleep(5)
    for item in list_arr:
        if '==' in item:
            continue
        print(f'Finding coupons for {item}')
        driver.find_element(By.XPATH, "/html/body/div[1]/section/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/form/input").clear()
        driver.find_element(By.XPATH, "/html/body/div[1]/section/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/form/input").send_keys(item)
        driver.find_element(By.XPATH, "/html/body/div[1]/section/div[4]/div/div[2]/div[1]/div[2]/div/div[1]/form/input").send_keys(Keys.ENTER)
        sleep(4)
        #TODO: Need to figure out how to get a list of Clip coupon buttons and click them using selenium
        clip_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Clip coupon')]")
        print(len(clip_buttons))
        if(len(clip_buttons) == 0):
            continue
        for clip_button in clip_buttons:
            clip_button.click()


def login_target(driver):
    print("Login in to Target..")
    load_dotenv()
    username = os.getenv('TARGET_USERID')
    pw = os.getenv('TARGET_PWD')
    driver.get('https://www.target.com/')
    sleep(3)
    driver.find_element(By.XPATH, "//*[@id=\"headerPrimary\"]/a[4]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[9]/div/div/div[2]/ul/li[1]/a").click()
    sleep(3)
    driver.find_element(By.XPATH, "//input[@name=\"username\"]").send_keys(username)
    sleep(2)
    driver.find_element(By.XPATH, "//input[@name=\"password\"]").send_keys(pw)
    sleep(1)
    driver.find_element(By.XPATH, "//button[@id=\"login\"]").click()
    sleep(10)


def apply_target_coupons(driver, list_arr):
    print("Applying Target coupons..")
    '''
    TODO: Need to find a good way to clip coupons in Target. At this time target 
    does not have a great way to clip coupons.
    '''
    pass

if __name__ == "__main__":
    
    list = get_list(PUBLIX)
    lines = list.split('\n')

    # Remove ☑ or ☐ from each line
    list_arr = [line.replace('☑', '').replace('☐', '').strip() for line in lines]
    print(list_arr)
    
    
    print('Starting Chrome Driver')
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    login_publix(driver)
    apply_publix_coupons(driver, list_arr)

    ''' 
    login_harris_teeters(driver)
    apply_harris_teeter_coupons(driver, list_arr)
    '''

