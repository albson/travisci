from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
 
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

desired_cap = {
    'platform': "OS X 10.11",
    'browserName': "firefox",
    'version': "44.0",
    'name': "TravisCI Sample Test"
}

driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_cap)

driver.get('https://www.google.com/')
driver.current_url
driver.page_source
time.sleep(5)
driver.quit()