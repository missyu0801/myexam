from time import sleep

import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure


@pytest.mark.usefixtures("setup")
class BaseClass:

    def assert_element_is_displayed(self, value):
        if value.is_displayed() == True:
            assert True
        else:
            self.attach_screenshot("Bug detected")
            assert False

    def assert_correct_text_is_displayed(self, value, expected):
        if value.text == expected:
            assert True
        else:
            self.attach_screenshot("Bug Detected")
            assert False

    def wait_until_element_is_displayed(self, test):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, test))).is_displayed()


    def verify_correct_url_is_displayed(self, value):
        assert self.driver.current_url == value
        self.attach_screenshot("url is displayed")


    def verify_correct_page_title_is_displayed(self, value):
        assert self.driver.title == value
        self.attach_screenshot("correct title is displayed")


    def close_tab(self, currenturl, windowopened):
        maintab = ""
        allTabs = self.driver.window_handles
        for tab in allTabs:
            self.driver.switch_to.window(tab)
            if (self.driver.current_url == currenturl):
                maintab = tab
            else:
                sleep(2)
                assert self.driver.current_url == windowopened
                self.attach_screenshot("window opened")
                sleep(2)
                self.driver.close()
        self.driver.switch_to.window(maintab)

    def attach_screenshot(self, value):
        allure.attach(self.driver.get_screenshot_as_png(), name=value, attachment_type=AttachmentType.PNG)

    def go_back(self, value):
        sleep(5)
        self.attach_screenshot("window opened")
        assert self.driver.title == value
        self.driver.execute_script("window.history.go(-1)")

