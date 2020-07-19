from PageObject.LoginPage import loginpage_footer
from utilities.BaseClass import BaseClass


class Test_LoginFooter(BaseClass):

    def test_Verify_elements_are_displayed_in_footer(self):
        login_footer = loginpage_footer.Test_loginpage_footer(self.driver)
        login_footer.privacy_policy_link_is_displayed()
        login_footer.service_agreement_link_is_displayed()
        login_footer.recommendation_link_is_displayed()
        self.attach_screenshot("Test Passed -- login footer links are displayed")

    def test_Verify_privacy_policy_link_can_be_opened(self):
        login_footer = loginpage_footer.Test_loginpage_footer(self.driver)
        login_footer.privacy_policy_link_is_opened()

    def test_Verify_service_agreement__link_can_be_opened(self):
        login_footer = loginpage_footer.Test_loginpage_footer(self.driver)
        login_footer.service_agreement_link_is_opened()

    def test_TC008_Verify_recommendation_link_can_be_opened(self):
        login_footer = loginpage_footer.Test_loginpage_footer(self.driver)
        login_footer.recommendation_link_is_opened()

    def test_TC009_Verify_helpdesk_link_can_be_opened(self):
        login_footer = loginpage_footer.Test_loginpage_footer(self.driver)
        login_footer.Helpdeskn_link_is_opened()
