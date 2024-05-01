from selenium.webdriver.common.by import By


class PurchasePage:

    def __init__(self, driver):
        self.driver = driver

    country = (By.XPATH, "//input[@id='country']")
    click_counntry = (By.XPATH, "//a[normalize-space()='India']")
    yes = (By.XPATH, "//a[normalize-space()='India']")
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button = (By.XPATH, "//input[@value='Purchase']")
    text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def setCountryName(self):
        return self.driver.find_element(*PurchasePage.country)

    def getCountry(self):
        return self.driver.find_element(*PurchasePage.click_counntry)

    def yesC(self):
        return self.driver.find_element(*PurchasePage.yes)

    def getCheckbox(self):
        return self.driver.find_element(*PurchasePage.checkbox)

    def getPurchase(self):
        return self.driver.find_element(*PurchasePage.purchase_button)

    def getText(self):
        return self.driver.find_element(*PurchasePage.text)