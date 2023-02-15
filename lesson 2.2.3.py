from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num1 = int(num1.text)
    num2 = browser.find_element(By.ID, "num2")
    num2 = int(num2.text)
    summa = num1 + num2
    summa = str(summa)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summa)

    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Su')]")
    button.click()
    time.sleep(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла