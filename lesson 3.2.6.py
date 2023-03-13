from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.google.com/")
browser.implicitly_wait(5)
assert browser.find_element(By.NAME, "btnK"), "Нет кнопки поиска"