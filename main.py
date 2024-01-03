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

def get_list():
    load_dotenv()
    user = os.getenv('KEEP_USER')
    pwd = os.getenv('KEEP_PWD')
    # print(user)
    # print(pwd)
    

    keep = gkeepapi.Keep()
    success = keep.login(user, pwd)

    if(success == True):
        gnotes = keep.get(os.getenv('KEEP_LIST'))
        # print(gnotes.title)
        # print(gnotes.text)
        return f'{gnotes.title} \n\n{gnotes.text}'


# TODO:TH Having issues login in to Harris Teeters. Fails auth/sigin
def login_harris_teeters(driver):
    load_dotenv()
    username = os.getenv('SHOP_USERID')
    pw = os.getenv('SHOP_PWD')
    driver.get("https://www.harristeeter.com/signin?redirectUrl=/savings/cl/coupons/")
    sleep(2)
    driver.find_element(By.XPATH, "//input[@name=\"email\"]").send_keys(username)
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name=\"password\"]").send_keys(pw)
    sleep(3)
    driver.find_element(By.XPATH, "//input[@name=\"password\"]").send_keys(Keys.ENTER)
    # driver.find_element(By.XPATH, "//input[@name=\"rememberMe\"]").click()
    # driver.find_element(By.XPATH, "//input[@name=\"termsAndConditions\"]").click()
    # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/main/section/section/section/form/button").click() # Login
    sleep(5)


def apply_harris_teeter_coupons(driver, list_arr):
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
    

if __name__ == "__main__":
    list = get_list()
    lines = list.split('\n')

    # Remove ☑ or ☐ from each line
    list_arr = [line.replace('☑', '').replace('☐', '').strip() for line in lines]
    print(list_arr)
    
    print('Starting Chrome Driver')
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--auto-open-devtools-for-tabs")
    # user_data_directory = '/Users/tommyho/Library/Application Support/Google/Chrome/Default'
    # options.add_argument(f'--user-data-dir={user_data_directory}')
    driver = uc.Chrome(options=options)
    driver.maximize_window()

    login_harris_teeters(driver)
    # sleep(6000)
    apply_harris_teeter_coupons(driver, list_arr)

