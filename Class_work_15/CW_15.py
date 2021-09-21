from selenium import webdriver
import time

def sel_habr():
    driver = webdriver.Safari()
    driver.get("https://account.habr.com/login/")
    element = driver.find_element_by_id("email_field")
    element.send_keys("denis.pilyaev@gmail.com")
    element = driver.find_element_by_id("password_field")
    element.send_keys("Pilya191092xzhukx")
    element = driver.find_element_by_class_name("button.button_wide.button_primary")
    element.click()
    time.sleep(5)
    driver.close()

sel_habr()