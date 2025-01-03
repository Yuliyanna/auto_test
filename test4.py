from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://onlinetestpad.com/ru/tests/informatics"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, "Python начальный тест")
    link.click()
    button = browser.find_element(By.CLASS_NAME, "clickable-element.bubble-element.Button.cnaSaUu")
    button.click()





finally:
    time.sleep(30)
    browser.quit()