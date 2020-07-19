from utilities import ConfigReader
from utilities.BaseClass import BaseClass
import allure

class Test_loginpage_footer(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    #Check Footer Elements are displayed
    @allure.description("Verify footer 'privacy policy' is displayed")
    @allure.severity(severity_level="MAJOR")
    def privacy_policy_link_is_displayed(self):
        privacypolicy = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("Footer", "privacy")))
        self.assert_element_is_displayed(privacypolicy)

    @allure.description("Verify footer 'service agreement' is displayed")
    @allure.severity(severity_level="MAJOR")
    def service_agreement_link_is_displayed(self):
        serviceagreement = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("Footer", "serviceagree")))
        self.assert_element_is_displayed(serviceagreement)

    @allure.description("Verify footer 'recommendation' is displayed")
    @allure.severity(severity_level="MAJOR")
    def recommendation_link_is_displayed(self):
        reco = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("Footer", "recommend")))
        self.assert_element_is_displayed(reco)

    #open footer links
    @allure.description("Verify 'privacy policy' link can be opened")
    @allure.severity(severity_level="MAJOR")
    def privacy_policy_link_is_opened(self):
        privacypolicy = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("Footer", "privacy")))
        privacypolicy.click()
        self.go_back("Privacy Policy")

    @allure.description("Verify 'service agreement'link can be opened")
    @allure.severity(severity_level="MAJOR")
    def service_agreement_link_is_opened(self):
        serviceagreement = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("Footer", "serviceagree")))
        serviceagreement.click()
        self.go_back("Paysera")

    @allure.description("Verify 'recommendation' link can be opened")
    @allure.severity(severity_level="MAJOR")
    def recommendation_link_is_opened(self):
        reco = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("Footer", "recommend")))
        reco.click()
        self.go_back("Recommendations for the safe use of Paysera")

    @allure.description("Verify New Window is opened when Helpdesk button is clicked")
    @allure.severity(severity_level="MAJOR")
    def Helpdeskn_link_is_opened(self):
        helpdesk = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("Footer", "helpdesk")))
        helpdesk.click()
        #self.close_tab("https://bank.paysera.com/en/login", "https://support.paysera.com/visitor/index.php?/payseraeng/LiveChat/Chat/Request/_sessionID=/_promptType=chat/_proactive=0/_filterDepartmentID=29/_randomNumber=n5i1laz54zo02b1iw72ptb3kh8492b5i/_fullName=/_email=/")