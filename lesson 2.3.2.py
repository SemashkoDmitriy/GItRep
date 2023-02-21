from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.execute_script("prompt('Humans at work');")
#alert = browser.switch_to.alert
#time.sleep(5)
#confirm = browser.switch_to.alert
#alert_text = confirm.text
#print(alert_text)
#confirm.dismiss()
prompt = browser.switch_to.alert
time.sleep(2)
prompt.send_keys("My answer")
time.sleep(5)
#prompt.accept()
time.sleep(3)