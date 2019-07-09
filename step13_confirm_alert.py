from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button1 = browser.find_element_by_css_selector("button.btn")
button1.click()

confirm = browser.switch_to.alert
confirm.accept()

input_value = browser.find_element_by_id("input_value")
result = calc(input_value.text)

input1 = browser.find_element_by_id("answer")
input1.send_keys(str(result))

button = browser.find_element_by_css_selector("button.btn")
button.click()