from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://testgrow.ru/course_main"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.ID, "sign_in")
    button1.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("bobrova.yuliya18@gmail.com")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[type='password']")
    input2.send_keys("yuliya1997")
    button = browser.find_element(By.CLASS_NAME, "clickable-element.bubble-element.Button.cnaSaUu")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
