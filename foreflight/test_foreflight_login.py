from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

valid_email = '[insert valid email]'
valid_pw = '[insert valid pw]'

invalid_email = '123@gamail.com'
invalid_pw = '123'

def test_fore_flight_login_with_valid_credentials():
    """ tests foreflight login with invalid credentials.
        login should be successful and display a 'logout' option on the page"""
    
    driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")

    # go to foreflight.com
    driver.get('https://www.foreflight.com')

    # find/ click 'login' button
    login_button = driver.find_element(By.ID, 'login')
    login_button.click()

    # find email txt box and type in user email
    email_txt_box = driver.find_element(By.ID, 'email')
    email_txt_box.send_keys(valid_email)

    # find pw txt box and type in user pw
    password_txt_box = driver.find_element(By.ID, 'password')
    password_txt_box.send_keys(valid_pw)

    # find/ click 'login' button
    login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/input')
    login_btn.click()

    # get page source
    page_source = driver.page_source

    # if successful, 'ForeFlight Web' should be driver title
    assert 'logout' in page_source
    
    
def test_fore_flight_login_with_invalid_email_and_pw():
    """ tests foreflight login with invalid credentials.
        login should be unsuccessful and display 'Invalid username or password' on the page"""

    driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")

    # go to foreflight.com
    driver.get('https://www.foreflight.com')

    # find/ click 'login' button
    login_button = driver.find_element(By.ID, 'login')
    login_button.click()

    # find email txt box and type in user email (not a real email)
    email_txt_box = driver.find_element(By.ID, 'email')
    email_txt_box.send_keys(invalid_email)

    # find pw txt box and type in user pw (not a real pw)
    password_txt_box = driver.find_element(By.ID, 'password')
    password_txt_box.send_keys(invalid_pw)

    # find/ click 'login' button
    login_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/input')
    login_btn.click()

    page_source = driver.page_source
    assert 'Invalid username or password' in page_source

def test_fore_flight_login_without_any_credentials():
    """ tests foreflight login with invalid credentials.
            login should be unsuccessful and display 'Invalid username or password' on the page"""

    driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")

    # go to foreflight.com
    driver.get('https://www.foreflight.com')

    # click 'login' button at top to take us to the login page
    driver.find_element(By.ID, 'login').click()

    # click login without typing in any credentials
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/input').click()

    page_source = driver.page_source

    assert 'Invalid username or password' in page_source
    
def test_fore_flight_login_with_valid_email_and_invalid_pw():
    """ tests foreflight login with valid email and invalid pw
        login should be unsuccessful and display, 'invalid username or password' on the page"""

    driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")
    # go to foreflight.com
    driver.get('https://www.foreflight.com')

    # click on 'login' button at top to take us to the login page
    driver.find_element(By.ID, 'login').click()

    # go to email input box and type in valid email
    driver.find_element(By.ID, 'email').send_keys(valid_email)

    # go to pw input box and type in INvalid pw
    driver.find_element(By.ID, 'password').send_keys(invalid_pw)

    # click on 'login' button
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/input').click()

    # get page source
    page_source = driver.page_source

    assert 'Invalid username or password' in page_source
