from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.udacity.com/')
print(driver.title)
time.sleep(30)

driver.quit()
