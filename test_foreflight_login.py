from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

def test_fore_flight_login():
    user_email = 'insert_user_email'
    user_pw = 'insert_user_pw'

    driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")

    # go to foreflight.com
    driver.get('https://www.foreflight.com')

    # find/ click 'login' button
    login_button = driver.find_element(By.ID, 'login')
    login_button.click()

    # find email txt box and type in user email
    email_txt_box = driver.find_element(By.ID, 'email')
    email_txt_box.send_keys(user_email)

    # find pw txt box and type in user pw
    password_txt_box = driver.find_element(By.ID, 'password')
    password_txt_box.send_keys(user_pw)

    # find/ click 'login' button
    login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/input')
    login_btn.click()

    # get title
    title = driver.title

    # if successful, 'ForeFlight Web' should be driver title
    assert driver.title == 'ForeFlight Web'

