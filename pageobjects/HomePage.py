from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    check_item = (By.XPATH, "//input[@id='exampleCheck1']")
    dropdown = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    item_I_Like = (By.XPATH, "//input[@id='inlineRadio2']")
    dob = (By.XPATH, "//input[@name='bday']")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckItem(self):
        return self.driver.find_element(*HomePage.check_item)

    def getDropDown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def getItemCheckBox(self):
        return self.driver.find_element(*HomePage.item_I_Like)

    def getDOB(self):
        return self.driver.find_element(*HomePage.dob)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertMSG(self):
        return self.driver.find_element(*HomePage.alert_msg)