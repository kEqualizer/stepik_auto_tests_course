from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value")
    x = int(x.text)

    result = math.log ( abs ( 12 * math.sin(x) ) )

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    submit_btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_btn.click()

finally:
    time.sleep(7)
    browser.quit()

