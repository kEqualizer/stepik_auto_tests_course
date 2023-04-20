from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys("Kir")

    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys("Navalny")

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("Navalny@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')

    send_btn = browser.find_element(By.ID, "file")
    send_btn.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(7)
    browser.quit()

