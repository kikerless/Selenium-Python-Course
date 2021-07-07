# from selenium import webdriver
# import time
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/math.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element_by_xpath("/html/body/div/form/div[1]/label/span[2]")
#     x = x_element.text
#     y = calc(x)
#     print(y)
#
#     answer = browser.find_elements_by_id("answer")
#     answer[0].send_keys(str(y))
#     # answer.send_keys(y)
#     captcha = browser.find_elements_by_id("robotCheckbox")
#     captcha[0].click()
#     robot = browser.find_elements_by_css_selector("[for='robotsRule']")
#     robot[0].click()
#     submit = browser.find_elements_by_class_name("btn-default")
#     submit[0].click()
#
# finally:
#     time.sleep(30)
#     browser.quit()


# from selenium import webdriver
# import time
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/get_attribute.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element_by_id("treasure")
#     x = x_element.get_attribute("valuex")
#     y = calc(x)
#     print(y)
#
#     answer = browser.find_elements_by_id("answer")
#     answer[0].send_keys(str(y))
#     # answer.send_keys(y)
#     captcha = browser.find_elements_by_id("robotCheckbox")
#     captcha[0].click()
#     robot = browser.find_element_by_id("robotsRule")
#     robot.click()
#     submit = browser.find_elements_by_class_name("btn-default")
#     submit[0].click()
#
# finally:
#     time.sleep(30)
#     browser.quit()

# from selenium import webdriver
# import time
# import math
# from selenium.webdriver.support.ui import Select
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/selects1.html"
# link2 = "http://suninjuly.github.io/selects2.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link2)
#
#     x_element = browser.find_element_by_id("num1").text
#     y_element = browser.find_element_by_id("num2").text
#     result = int(x_element) + int(y_element)
#     print(result)
#
#     select = Select(browser.find_element_by_tag_name("select"))
#     select.select_by_value(str(result))
#
#     browser.find_element_by_class_name("btn-default").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# import time
# import math
# from selenium.webdriver.support.ui import Select
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# link = "http://suninjuly.github.io/execute_script.html"
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x = browser.find_element_by_id("input_value").text
#     result = calc(x)
#     print(result)
#
#     browser.execute_script("window.scrollBy(0, 100);")
#     answer = browser.find_element_by_id("answer").send_keys(str(result))
#     captcha = browser.find_element_by_id("robotCheckbox").click()
#     robot = browser.find_element_by_id("robotsRule").click()
#     browser.find_element_by_class_name("btn-primary").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# import time
# import os
#
# link = "http://suninjuly.github.io/file_input.html"
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_name("firstname").send_keys("Aloha")
#     browser.find_element_by_name("lastname").send_keys("Ahola")
#     browser.find_element_by_name("email").send_keys("Ahola@Aloha.loh")
#
#     current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#     file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
#     browser.find_element_by_name("file").send_keys(file_path)
#
#     browser.find_element_by_class_name("btn-primary").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# import time
# import math
#
# link = "http://suninjuly.github.io/alert_accept.html"
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_class_name("btn-primary").click()
#
#     alert = browser.switch_to.alert
#     alert.accept()
#
#     x = browser.find_element_by_id("input_value").text
#     result = calc(x)
#     print(result)
#
#     browser.find_element_by_id("answer").send_keys(str(result))
#
#     browser.find_element_by_class_name("btn-primary").click()
#
#     alert = browser.switch_to.alert.text
#     print(alert)
#
# finally:
#     time.sleep(10)
#     browser.quit()


# from selenium import webdriver
# import time
# import math
#
# link = "http://suninjuly.github.io/redirect_accept.html"
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     browser.find_element_by_class_name("btn-primary").click()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(new_window)
#
#     x = browser.find_element_by_id("input_value").text
#     result = calc(x)
#     print(result)
#
#     browser.find_element_by_id("answer").send_keys(str(result))
#
#     browser.find_element_by_class_name("btn-primary").click()
#
#     alert = browser.switch_to.alert.text
#     print(alert)
#
# finally:
#     time.sleep(10)
#     browser.quit()


from selenium import webdriver
import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 12)
    element = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element_by_id("book").click()

    x = browser.find_element_by_id("input_value").text
    result = calc(x)
    print(result)
    browser.find_element_by_id("answer").send_keys(str(result))
    browser.find_element_by_id("solve").click()
    alert = browser.switch_to.alert.text
    print(alert)

finally:
    time.sleep(10)
    browser.quit()