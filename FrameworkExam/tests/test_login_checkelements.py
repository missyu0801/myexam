import pytest


from PageObject.LoginPage import loginpage_check_elements
from PageObject.LoginPage import test_login
from utilities.BaseClass import BaseClass


class Test_LoginPage(BaseClass):

    def test_Verify_side_panels_elements_are_displayed(self):
        login_page = loginpage_check_elements.Test_loginpage_elements(self.driver)
        login_page.sidebar_is_displayed()
        login_page.logo_is_displayed()
        login_page.login_banner_is_displayed()
        login_page.banner_description_is_displayed()
        login_page.googleplay_button_is_displayed()
        self.attach_screenshot("Test Passed -- sidebar is displayed")

    def test_Verify_elements_in_login_panel_are_visible(self):
        login_panel = test_login.Test_login_panel(self.driver)
        login_panel.login_panel_is_displayed()
        login_panel.user_identifier_textbox_is_displayed()
        login_panel.login_button_is_displayed()
        login_panel.Register_Now_link_is_displayed()
        self.attach_screenshot("Test Passed -- login panels are displayed")


    def test_Verify_another_window_opened_when_googleplay_button_is_clicked(self):
        login_page = loginpage_check_elements.Test_loginpage_elements(self.driver)
        login_page.googleplay_button_is_clicked()

    def test_Verify_another_window_opened_when_appstore_button_is_clicked(self):
        login_page = loginpage_check_elements.Test_loginpage_elements(self.driver)
        login_page.appstore_button_is_clicked()

    def test_Verify_register_now_link_can_be_opened(self):
        login_panel = test_login.Test_login_panel(self.driver)
        login_panel.register_now_link_can_be_opened()


