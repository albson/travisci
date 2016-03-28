#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import os
from selenium import webdriver
import sys

# Retreiving enviroment variables
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

desired_capabilities = {}
desired_capabilities['platform'] = 'linux'
desired_capabilities['version'] = '44'
desired_capabilities['browserName'] = 'Chrome'


driver = webdriver.Remote(command_executor = ('http://' + SAUCE_USERNAME + ':' + SAUCE_ACCESS_KEY + '@ondemand.saucelabs.com:80/wd/hub'), desired_capabilities = desired_capabilities)
driver.implicitly_wait(30)

driver.get('http://google.com')
title = driver.title
assert "Google", title

time.sleep(10)

driver.get('https://www.saucelabs.com')
title = driver.title
assert "Sauce Labs: Selenium Testing, Mobile Testing, JS Unit Testing and More", title

time.sleep(10)

driver.get('http://www.theuselessweb.com/')
title = driver.title
assert "The Useless Web", title

driver.quit()