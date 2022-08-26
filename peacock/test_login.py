from selenium import webdriver
from selenium.webdriver.common.by import By
import time

valid_email = 'enter_a_valid_email'
valid_pw = 'enter_a_valid_pw'

def test_peacocktv_login_with_valid_credentials():
    driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")

    driver.get('https://www.peacocktv.com/')
    #time.sleep(3)
    driver.implicitly_wait(10)

    # find/ click 'sign in' button
    driver.find_element(By.CLASS_NAME, 'ib-sk-button-text').click()

    # find email text box, type in valid email
    driver.find_element(By.ID, 'userIdentifier').send_keys(valid_email)

    # find pw text box, type in valid pw
    driver.find_element(By.ID, 'password').send_keys(valid_pw)

    # keep signed in is defaulted to True: click this box to set it to False
    driver.find_element(By.ID, 'rememberMe').click()

    # click sign in button
    driver.find_element(By.CLASS_NAME, 'sign-in-form__buttons').click()
    
    # not done.. just ran out of time
    # still need to verify that login worked

    time.sleep(5)
