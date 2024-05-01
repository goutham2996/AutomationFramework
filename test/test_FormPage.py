import time

from selenium.webdriver.support.select import Select

from pageobjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestFormPage(BaseClass):

    def test_formPage(self):

        url = "https://rahulshettyacademy.com/angularpractice/"
        name = "Goutham"
        email = "gautamspikee@gmail.com"
        password = "abc@123"
        gender = "Male"
        dob = "29081996"

        self.driver.get(url)
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(name)
        homePage.getEmail().send_keys(email)
        homePage.getPassword().send_keys(password)
        homePage.getCheckItem().click()
        assert homePage.getCheckItem().is_selected()
        dropdown = Select(homePage.getDropDown())
        dropdown.select_by_visible_text(gender)
        homePage.getCheckItem().click()
        assert homePage.getCheckItem().is_enabled()
        homePage.getDOB().send_keys(dob)
        homePage.getSubmitButton().click()
        self.driver.execute_script("window.scrollTo(0,0);")
        time.sleep(2)
        text_msg_displayed = homePage.getAlertMSG().text
        assert "Success" in text_msg_displayed






