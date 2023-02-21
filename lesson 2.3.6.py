from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import math

link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #Открываем страницу адрес которой находится в переменной link под управлением selenium webdriver
    browser = webdriver.Chrome()
    browser.get(link)

    #находим элемент кнопка на открытой странице и нажимаем на нее, используя метод click()
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    #Переключаемся на вновь открывшуюся вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    print(new_window)

    #Находим элемент для ввода ответа на каптчу, вставлем вычисленный ответ и нажимаем на кнопку отправить
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[contains(text(), 'Su')]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()