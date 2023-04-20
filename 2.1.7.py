from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    picture = browser.find_element(By.ID, "treasure")
    x_element = picture.get_attribute("valuex")
    x = x_element
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