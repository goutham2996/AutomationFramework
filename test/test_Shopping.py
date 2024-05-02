import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.ConfirmPage import ConfirmPage
from pageobjects.HomePage import HomePage
from pageobjects.PurchasePage import PurchasePage
from pageobjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestShopping(BaseClass):

    def test_shopping(self):
        url = "https://rahulshettyacademy.com/angularpractice/"
        country_name = "ind"
        country_to_select = "India"

        self.driver.get(url)
        homePage = HomePage(self.driver)
        homePage.shopLink().click()

        shopPage = ShopPage(self.driver)
        phones = shopPage.getPhones()
        for i in phones:
            if i.find_element(By.XPATH, "div/h4/a").text == "Samsung Note 8":
                i.find_element(By.XPATH, "div/button").click()

        shopPage.getCheckout().click()

        confirmPage = ConfirmPage(self.driver)
        confirmPage.getCheckout().click()

        purchasePage = PurchasePage(self.driver)
        purchasePage.setCountryName().send_keys(country_name)

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[normalize-space()='India']")))

        purchasePage.yesC().click()
        purchasePage.getCheckbox().click()
        purchasePage.getPurchase().click()
        text = purchasePage.getText().text
        assert "Success" in text
        time.sleep(2)




