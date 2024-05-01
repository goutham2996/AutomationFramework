from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    phones = (By.XPATH, "//div[@class='card h-100']")
    checkout = (By.XPATH, "//a[@class='nav-link btn btn-primary']")

    def getPhones(self):
        return self.driver.find_elements(*ShopPage.phones)

    def getCheckout(self):
        return self.driver.find_element(*ShopPage.checkout)


