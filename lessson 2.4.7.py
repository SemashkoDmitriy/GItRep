from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import time

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button = browser.find_element(By.ID, "book")
button.click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
answer = browser.find_element(By.CSS_SELECTOR, "#answer")
answer.send_keys(y)
button = browser.find_element(By.XPATH, "//button[contains(text(), 'Su')]")
button.click()
# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()