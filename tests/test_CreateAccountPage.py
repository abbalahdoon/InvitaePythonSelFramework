from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.CreateAccountPage import CreateAccountPage
from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass


class TestCreateAccountPage(BaseClass):

#Verify user is not able to create an account with a registered email address
    def test_CreateAccountWithRegisteredUser(self):
        log = self.getLogger()
        signInpage = SignInPage(self.driver)
        signInpage.gotoSignInPage()
        createaccountpage = CreateAccountPage(self.driver)
        createaccountpage.getEmail().send_keys("tubaozden@gmail.com")
        log.info("email address is")

        createaccountpage.clickCreateAccountButton()
        self.verifyElementPresence("xpath", "//div[@id='create_account_error']//li")
        alertText = createaccountpage.getErrorMessage().text

        log.info("Text received from application is " + alertText)
        assert ("has already been registered" in alertText)

    def  test_CreateAccount(self):
        log = self.getLogger()
        signInpage = SignInPage(self.driver)
        signInpage.gotoSignInPage()
        createaccountpage = CreateAccountPage(self.driver)
        createaccountpage.getEmail().send_keys("toturkay@gmail.com")
        log.info("email address is")
        createaccountpage.clickCreateAccountButton()
        #self.verifyElementPresence("xpath", "//div[@id='create_account_error']//li")
        createaccountpage.clickCreateAccountButton()


