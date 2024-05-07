import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.LoginForm import LoginForm
from utilities.BaseClass import BaseClass


class TestLoginForm(BaseClass):

    def test_LoginForm(self):
        url = "https://rahulshettyacademy.com/loginpagePractise/"
        self.driver.get(url)

        loginForm = LoginForm(self.driver)
        loginForm.getName().send_keys("rahulshettyacademy")
        loginForm.getPass().send_keys("1234")
        loginForm.getButton().click()
        loginForm.getSubmitButton().click()
        wait = WebDriverWait(self.driver, 6)
        wait.until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")))

        print(self.driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text)
        time.sleep(2)



