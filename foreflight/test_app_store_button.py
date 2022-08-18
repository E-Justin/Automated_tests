from selenium import webdriver
from selenium.webdriver.common.by import By

def test_app_store_button_on_login_page_by_url_after_click():
    driver = webdriver.Chrome('C:\webDrivers\chromedriver.exe')
    
    # go to foreflight.com
    driver.get('https://www.foreflight.com')

    # store id of original window (after clicking on app store button, a new window will open, taking us to a new site)
    original_window = driver.current_window_handle
    
    # had some issues with things not loading in time, so this is the fix
    driver.implicitly_wait(10)
    
    # find/ click on app store button
    driver.find_element(By.XPATH, '//*[@id="carousel-1"]/div/div[1]/div/div/div/div[1]/figure/a/img').click()

    # find new window handle
    for window_handle in driver.window_handles:  # loop through window handles
        if window_handle != original_window:  # find new window handle
            driver.switch_to.window(window_handle)  # switch to new handle
    
    # this should be the url in the new window if it worked properly
    assert driver.current_url == 'https://apps.apple.com/us/app/foreflight-mobile-3/id333252638'
