from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from pageObjects.AuthenticationPage import AuthenticationPage
from utilities.BaseClass import BaseClass


class TestAuthenticationPage(BaseClass):

    #Verify user is not able to sign in with invalid credentials
    def test_signInWithInvalidCredentials(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmail().send_keys("tubaozden@gmail.com")
        authenticationpage.getPassword().send_keys("password")
        authenticationpage.clickSignInButton()
        errorMessage = authenticationpage.getErrorMessage().text
        log.info("Error Message is: " + errorMessage)
        assert ("Authentication failed" in errorMessage)

        self.driver.refresh()

    # #@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    # def getData(self, request):
    #     return request.param

    # Verify error message is displayed when user creates an account with already existing email address
    def test_createAccountWithRegisteredUser(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmailCreateAccount().send_keys("tubaozden@gmail.com")
        log.info("email address is tubaozden@gmail.com")
        authenticationpage.clickCreateAccountButton()
        self.verifyElementPresence("xpath", "//div[@id='create_account_error']//li")
        errMessageAlreadyRegistered = authenticationpage.getErrorMessageAlreadyRegistered().text
        log.info("Text received from application is " + errMessageAlreadyRegistered)
        assert ("has already been registered" in errMessageAlreadyRegistered)

    # Verify user is able to sign in with valid credentials
    def test_signInWithValidCredentials(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmail().send_keys("tugbaozden@gmail.com")
        authenticationpage.getPassword().send_keys("12345")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", authenticationpage.getSignInButton())
        authenticationpage.clickSignInButton()
        welcomeMessage = authenticationpage.getWelcomeMessage().text
        if "Welcome" in welcomeMessage:
            log.info("User is successfully signed in")
        else:
            log.info("User is NOT successfully signed in")

    #Verify user is able to sign out successfully
    #@pytest.fixture(scope="session")
    def test_signOut(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmail().send_keys("tugbaozden@gmail.com")
        authenticationpage.getPassword().send_keys("12345")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", authenticationpage.getSignInButton())
        authenticationpage.clickSignInButton()
        self.verifyElementPresence("css", "p.info-account")
        authenticationpage.clickSignOutButton()
        self.verifyElementPresence("css", "a.login")
        assert authenticationpage.getLogin().get_attribute("class") == "login"
        log.info("User is successfully signed out")






