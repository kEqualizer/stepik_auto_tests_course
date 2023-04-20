from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    num = browser.find_element(By.ID, "input_value")
    result = math.log(abs(12*math.sin(int(num.text))))

    input = browser.find_element(By.ID, "answer")
    input.send_keys(result)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio_btn = browser.find_element(By.ID, "robotsRule")
    radio_btn.click()

    button.click()

finally:
    time.sleep(7)
    browser.quit()

