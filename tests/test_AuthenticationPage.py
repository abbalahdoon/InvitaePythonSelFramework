from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.AuthenticationPageData import AuthenticationPageData
from pageObjects.HomePage import HomePage
from pageObjects.AuthenticationPage import AuthenticationPage
from utilities.BaseClass import BaseClass


class TestAuthenticationPage(BaseClass):

    #Verify that user is not able to sign in with invalid credentials
    def test_signInWithInvalidCredentials(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmail().send_keys("tubaozden@gmail.com")
        authenticationpage.getPassword().send_keys("password")
        authenticationpage.clickSignInButton()
        errorMessage = authenticationpage.getErrorMessage().text
        log.info("User is able to view error message successfully. Error Message is: " + errorMessage)
        assert ("Authentication failed" in errorMessage)

        self.driver.refresh()

    # Verify that an error message is displayed when user creates an account with already existing email address
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

    # Verify that user is able to sign in with valid credentials
    def test_signInWithValidCredentials(self,getData):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmail().send_keys(getData["emailaddress"])
        authenticationpage.getPassword().send_keys(getData["password"])
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", authenticationpage.getSignInButton())
        authenticationpage.clickSignInButton()
        welcomeMessage = authenticationpage.getWelcomeMessage().text
        if "Welcome" in welcomeMessage:
            log.info("User is successfully signed in with valid credentials")
        else:
            log.info("User is NOT successfully signed in")

    #Verify that user is able to sign out successfully
    #@pytest.fixture(scope="session")
    def test_signOut(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        authenticationpage.clickSignOutButton()
        self.verifyElementPresence("css", "a.login")
        assert authenticationpage.getLogin().get_attribute("class") == "login"
        log.info("User is successfully signed out")

    @pytest.fixture(params=AuthenticationPageData.test_AuthenticationPage_data)
    def getData(self, request):
        return request.param





