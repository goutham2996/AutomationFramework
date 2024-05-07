import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("D:\Softwares\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "edge":
        service_obj = Service("D:\Softwares\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser_name == "IE":
        print("IE driver")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


