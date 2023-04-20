from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    option_checkbox = browser.find_element(By.ID, "robotCheckbox")
    option_checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button_submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()