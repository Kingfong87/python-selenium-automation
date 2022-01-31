from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/Fchue/Automation/python-selenium-automation/chromedriver.exe')

driver.get('https://www.amazon.com/gp/help/costumer/display.html')

driver.find_element(By.Id, 'helpsearch').send_keys('cancel orders', keys.Enter)

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content'] /h1"). text
expected_text= 'cancel items or orders'

assert expected_text == actual_text, f'expected {expected_text}, but got {actual_text}'

driver.quit()