from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def test1():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.XPATH,
                                  "//div[@class='first_block']/div/label[text()='First name*']//following-sibling::input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH,
                                  "//div[@class='first_block']/div/label[text()='Email*']//following-sibling::input")
    input2.send_keys("email@mail.ru")
    input3 = browser.find_element(By.XPATH,
                                  "//div[@class='second_block']/div/label[text()='Phone:']//following-sibling::input")
    input3.send_keys("9063571336")
    input4 = browser.find_element(By.XPATH,
                                  "//div[@class='second_block']/div/label[text()='Address:']//following-sibling::input")
    input4.send_keys("Перевоз")

    time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

def test2():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element(By.XPATH,
                                  "//div[@class='first_block']/div/label[text()='First name*']//following-sibling::input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH,
                                  "//div[@class='first_block']/div/label[text()='ast name*']//following-sibling::input")
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.XPATH,
                                  "//div[@class='first_block']/div/label[text()='Email*']//following-sibling::input")
    input3.send_keys("email@mail.ru")
    input4 = browser.find_element(By.XPATH,
                                  "//div[@class='second_block']/div/label[text()='Phone:']//following-sibling::input")
    input4.send_keys("9063571336")
    input5 = browser.find_element(By.XPATH,
                                  "//div[@class='second_block']/div/label[text()='Address:']//following-sibling::input")
    input5.send_keys("Перевоз")

    time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element(By.XPATH, "//button[text()='Submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    pytest.main()

