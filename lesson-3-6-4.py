import time
import math
from tkinter import END

from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, links):
    browser.get(links)
    #try:
    browser.find_element(By.ID, "ember33").click()
    login = browser.find_element(By.ID, "id_login_email")
    login.send_keys("semashko@fgoupsk.ru")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("preventer")
    btn = browser.find_element(By.CLASS_NAME, "button_with-loader")
    btn.click()
    print('11111111')
    time.sleep(3)
    answer = str(math.log(int(time.time() + 23.3)))
    print('22222222')
    field = browser.find_element(By.CLASS_NAME, "ember-text-area")
    field.clear()
    print('44444444')
    #time.sleep(3)
    field.send_keys(answer)
    print('55555555')
    button = browser.find_element(By.CLASS_NAME, "submit-submission")
    print('66666666')
    button.click()
    message = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert message.text == "Correct!", print(message)

    #except:
        #answer = math.log(int(time.time()))
        #print(answer)
        #field = browser.find_element(By.ID, "ember87")
        #field.send_keys(str(answer))
        #button = WebDriverWait(browser, 5).until(
        #    EC.element_to_be_clickable(By.CLASS_NAME, "submit-submission"))
        #button.click()
        #time.sleep(5)