import pytest


from utilities.BaseClass import BaseClass
from utilities import Testdata
from PageObject.LoginPage import test_login

class Test_Login_Data(BaseClass):

    @pytest.mark.parametrize('data', Testdata.invalid_username())
    def test_Verify_error_displayed_when_invalid_username_entered(self,data):
        login_panel = test_login.Test_login_panel(self.driver)
        login_panel.enter_user_credential(data[0])
        login_panel.click_login_button()
        login_panel.verify_error_is_displayed_invalid_username_input()
        self.driver.refresh()

    @pytest.mark.parametrize('data', Testdata.valid_data())
    def test_Verify_user_can_login_successfully(self, data):
        login_panel = test_login.Test_login_panel(self.driver)
        login_panel.enter_user_credential(data[0])
        login_panel.click_login_button()
        login_panel.enter_password(data[1])
        login_panel.click_login_button()
        login_panel.verify_user_can_logout()

    @pytest.mark.parametrize('data', Testdata.valid_un_invalid_pw())
    def test_Verify_error_displayed_when_invalid_password_entered(self, data):
        login_panel = test_login.Test_login_panel(self.driver)
        login_panel.enter_user_credential(data[0])
        login_panel.click_login_button()
        login_panel.enter_password(data[1])
        login_panel.click_login_button()
        login_panel.verify_error_is_displayed_invalid_password_input()
        login_panel.click_pencil_icon()
        self.driver.refresh()




