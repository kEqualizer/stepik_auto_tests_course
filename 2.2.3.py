from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    result = int(num1) + int(num2)
    print(result)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))

    submit_btn = browser.find_element(By.TAG_NAME, "button")
    submit_btn.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()