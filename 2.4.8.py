import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    x = browser.find_element(By.ID, "input_value")
    x = int(x.text)

    result = math.log ( abs ( 12 * math.sin(x) ) )

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    submit_btn = browser.find_element(By.ID, "solve")
    submit_btn.click()

finally:
    time.sleep(20)
    browser.quit()