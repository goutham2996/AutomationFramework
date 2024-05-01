from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//button[normalize-space()='Checkout']")
    def getCheckout(self):
        return self.driver.find_element(*ConfirmPage.checkout)