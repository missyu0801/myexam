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
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "edge":
        driver = webdriver.Edge()

    driver.get(ConfigReader.read_config_data("Details", "LoginPage_url"))
    driver.maximize_window()
    request.cls.driver = driver
    driver.implicitly_wait(50)
    assert driver.title == "Log in to your account - Paysera"

    yield
    driver.close()
