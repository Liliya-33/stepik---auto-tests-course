from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
button = browser.find_element_by_id('book')
button.click()
num = browser.find_element_by_id('input_value')
x = num.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


y = calc(x)
input1 = browser.find_element_by_id("answer")  # находим элемент
input1.send_keys(y)

button = browser.find_element_by_css_selector('[type="submit"]')
button.click()