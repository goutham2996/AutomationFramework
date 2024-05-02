import time

import pytest
from _pytest.mark import param
from selenium.webdriver.support.select import Select

from pageobjects.HomePage import HomePage
from testdata.HomePage import HomePageTestData
from utilities.BaseClass import BaseClass


class TestFormPage(BaseClass):

    def test_formPage(self, getData):

        url = "https://rahulshettyacademy.com/angularpractice/"
        #name = "Goutham"
        #email = "gautamspikee@gmail.com"
        password = "abc@123"
        gender = "Male"
        dob = "29081996"

        self.driver.get(url)
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["uname"])
        homePage.getEmail().send_keys(getData["uemail"])
        homePage.getPassword().send_keys(getData["upassword"])
        homePage.getCheckItem().click()
        assert homePage.getCheckItem().is_selected()
        dropdown = Select(homePage.getDropDown())
        dropdown.select_by_visible_text(getData["ugender"])
        homePage.getCheckItem().click()
        assert homePage.getCheckItem().is_enabled()
        homePage.getDOB().send_keys(getData["udob"])
        homePage.getSubmitButton().click()
        self.driver.execute_script("window.scrollTo(0,0);")
        time.sleep(2)
        text_msg_displayed = homePage.getAlertMSG().text
        assert "Success" in text_msg_displayed

    @pytest.fixture(params=HomePageTestData.test_data_test_Form)
    def getData(self, request):
            return request.param






