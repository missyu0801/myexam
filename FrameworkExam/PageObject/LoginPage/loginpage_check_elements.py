from utilities import ConfigReader
from utilities.BaseClass import BaseClass
import allure


class Test_loginpage_elements(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    #Check Elements are displayed
    @allure.title("Verify sidebar is displayed")
    @allure.severity(severity_level="MAJOR")
    def sidebar_is_displayed(self):
        side = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "sidebar")))
        self.assert_element_is_displayed(side)


    @allure.description("Verify logo is displayed")
    @allure.severity(severity_level="MAJOR")
    def logo_is_displayed(self):
        logo = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "logo")))
        self.assert_element_is_displayed(logo)


    @allure.description("Verify login banner is displayed")
    @allure.severity(severity_level="MAJOR")
    def login_banner_is_displayed(self):
        lbanner = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "lbanner")))
        self.assert_correct_text_is_displayed(lbanner, "The Paysera mobile application – for more convenient use")

    @allure.description("Verify loggin banner description is displayed")
    @allure.severity(severity_level="MAJOR")
    def banner_description_is_displayed(self):
        bdescription = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "bannerdescription")))
        self.assert_correct_text_is_displayed(bdescription, "Check your account balance, perform bank transfers with a few clicks, exchange currency, "
                                                            "send money requests to friends and try other convenient features with the Paysera Mobile App.")

    @allure.description("Verify appstore button is displayed")
    @allure.severity(severity_level="MAJOR")
    def appstore_btn_is_displayed(self):
        appstore = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "appstorebtn")))
        self.assert_element_is_displayed(appstore)

    @allure.description("Verify googleplay button is displayed")
    @allure.severity(severity_level="MAJOR")
    def googleplay_button_is_displayed(self):
        googleplay = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "googleplaybtn")))
        self.assert_element_is_displayed(googleplay)

    #When user clicks appstore or googleplay button in side tab
    @allure.description("Verify appstore window is displayed when appstore button is clicked")
    @allure.severity(severity_level="MAJOR")
    def appstore_button_is_clicked(self):
        appstore = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "appstorebtn")))
        appstore.click()
        #self.wait_until_element_is_displayed("//span[contains(text(),'App Store')]")
        self.close_tab("https://bank.paysera.com/en/login",
                       "https://apps.apple.com/app/paysera-mobile-wallet/id737308884")


    @allure.description("Verify googleplay window is displayed when googleplay button is clicked")
    @allure.severity(severity_level="MAJOR")
    def googleplay_button_is_clicked(self):
        googleplay = self.driver.find_element_by_xpath((ConfigReader.read_login_elements("LoginElements", "googleplaybtn")))
        googleplay.click()
        #self.wait_until_element_is_displayed("//a[@title='Google Play Logo']")
        self.close_tab("https://bank.paysera.com/en/login", "https://play.google.com/store/apps/details?id=lt.lemonlabs.android.paysera")
