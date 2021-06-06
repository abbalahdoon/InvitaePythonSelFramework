from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.CreateAccountPage import CreateAccountPage
from pageObjects.HomePage import HomePage
from pageObjects.AuthenticationPage import AuthenticationPage
from utilities.BaseClass import BaseClass


class TestCreateAccountPage(BaseClass):

#Verify user is not able to create an account with a registered email address


    def  test_CreateAccount(self):
        log = self.getLogger()
        signInpage = AuthenticationPage(self.driver)
        signInpage.goToAuthenticationPage()
        createaccountpage = CreateAccountPage(self.driver)
        createaccountpage.getEmail().send_keys("toturkay@gmail.com")
        log.info("email address is")
        createaccountpage.clickCreateAccountButton()
        self.verifyElementPresence("xpath", "//h1[contains(text(), 'Create')]")



