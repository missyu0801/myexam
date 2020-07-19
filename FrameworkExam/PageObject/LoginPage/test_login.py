from time import sleep

from utilities import ConfigReader
from utilities.BaseClass import BaseClass
import allure


class Test_login_panel(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    #input username and password
    @allure.description("Verify user can enter user login data")
    @allure.severity(severity_level="CRITICAL")
    def enter_user_credential(self, value):
        un = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "usernamelogin")))
        un.send_keys(value)
        self.attach_screenshot("data was entered")

    @allure.description("Verify user can enter password data")
    @allure.severity(severity_level="CRITICAL")
    def enter_password(self, value):
        pw = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "password")))
        pw.send_keys(value)
        self.attach_screenshot("data was entered")

    @allure.description("Verify user can click login button")
    @allure.severity(severity_level="CRITICAL")
    def click_login_button(self):
        loginbutton = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "loginbutton")))
        loginbutton.click()

    @allure.description("Verify user can go back to input username")
    @allure.severity(severity_level="Major")
    def click_pencil_icon(self):
        pencilicon = self.driver.find_element_by_xpath(
            (ConfigReader.read_login_elements("LoginElements", "pencilicon")))
        pencilicon.click()

    @allure.description("Verify user can logout")
    @allure.severity(severity_level="Major")
    def verify_user_can_logout(self):
        signout = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "logout")))
        signout.click()


    #login panel elements checking
    @allure.description("Verify login panel is displayed")
    @allure.severity(severity_level="MAJOR")
    def login_panel_is_displayed(self):
        lpanel = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "loginpanel")))
        self.assert_element_is_displayed(lpanel)

    @allure.description("Verify user identifier textbox is displayed")
    @allure.severity(severity_level="MAJOR")
    def user_identifier_textbox_is_displayed(self):
        usernamelogin = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "usernamelogin")))
        self.assert_element_is_displayed(usernamelogin)

    @allure.description("Verify signup button is displayed")
    @allure.severity(severity_level="MAJOR")
    def login_button_is_displayed(self):
        loginbutton = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "usernamelogin")))
        self.assert_element_is_displayed(loginbutton)

    @allure.description("Verify register now button is displayed")
    @allure.severity(severity_level="MAJOR")
    def Register_Now_link_is_displayed(self):
        regnow = self.driver.find_element_by_xpath(
            (ConfigReader.read_login_elements("LoginElements", "registernowlnktxt")))
        self.assert_element_is_displayed(regnow)

    # Click Register Now
    @allure.description("Verify footer 'recommendation' is displayed")
    @allure.severity(severity_level="MAJOR")
    def register_now_link_can_be_opened(self):
        regnow = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "registernowlnktxt")))
        regnow.click()
        self.attach_screenshot("window opened")
        self.go_back("Account Registration - Paysera")


    #verify error messages
    @allure.description("Verify error message is displayed when invalid user is entered")
    @allure.severity(severity_level="CRITICAL")
    def verify_error_is_displayed_invalid_username_input(self):
        invaliduser= self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "error")))
        self.assert_correct_text_is_displayed(invaliduser, "The specified user could not be found")
        self.attach_screenshot("Error Message is displayed")


    @allure.description("Verify error message is displayed when invalid password is entered")
    @allure.severity(severity_level="CRITICAL")
    def verify_error_is_displayed_invalid_password_input(self):
        invalidpass = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "error")))
        self.assert_correct_text_is_displayed(invalidpass, "Incorrect password. Please try again.")
        self.attach_screenshot("Error Message is displayed")
