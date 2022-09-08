from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

valid_email = 'enter valid email here'
valid_pw = 'enter valid pw here'

def test_side_panel_button_flights():
  """ This tests that pushing the 'Flights' button in the side panel 
    of the main page of the web app, leads you to the correct page """
    driver = webdriver.Chrome("C:\webDrivers\chromedriver.exe")
    
    # 1. go to foreflight.com
    driver.get('https://www.foreflight.com')

    # 2. find/ click login button to go to login page
    driver.find_element(By.ID, 'login').click()

    driver.implicitly_wait(10)

    # 3. find email text box and type in valid email
    driver.find_element(By.ID, 'email').send_keys(valid_email)

    # 4. find pw text box and type in valid pw
    driver.find_element(By.ID, 'password').send_keys(valid_pw)

    # 5. find 'login' button and click it
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/form/div/div[3]/input').click()

    # 6. find 'Flights' button and click it
    driver.find_element(By.ID, 'web-trips').click()
    
    # 7. current url should change to {{base_url}}/flights...
    assert driver.current_url == 'https://plan.foreflight.com/flights/a668458f-a6a1-42c0-b798-1e9270e42c21/F58E0722D16142D99CA0C25EC361DFDC'

   
