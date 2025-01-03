from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://testgrow.ru/course_main"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, "Знакомство")
    link.click()
finally:
    time.sleep(30)
    browser.quit()
