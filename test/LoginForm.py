import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("D:\Softwares\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("leang")
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > form:nth-child(1) > div:nth-child(4) > div:nth-child(1) > label:nth-child(1) > span:nth-child(3)").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")))
print(driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text)
time.sleep(2)