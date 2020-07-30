from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
import pytest
from selenium import webdriver
from utilities import ConfigReader


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        path = "./Drivers/chromedriver.exe"
        driver = Chrome(executable_path=path)

    elif browser_name == "firefox":
        path1 = "./Drivers/geckodriver.exe"
        driver = webdriver.Firefox(executable_path=path1)

    elif browser_name == "edge":
        path2 = "./Drivers/MicrosoftWebDriver.exe"
        driver = webdriver.Edge(executable_path=path2)


    driver.get(ConfigReader.read_config_data("Details", "LoginPage_url"))
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(50)
    assert driver.title == "Log in to your account - Paysera"

    yield
    driver.close()
