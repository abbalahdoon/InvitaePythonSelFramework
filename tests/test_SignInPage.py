
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from pageObjects.SignInPage import SignInPage
from utilities.BaseClass import BaseClass


class TestSignInPage(BaseClass):

    def test_SignIn(self):
        log = self.getLogger()
        signInpage = SignInPage(self.driver)
        signInpage.gotoSignInPage()
        signInpage.getEmail().send_keys("tubaozden@gmail.com")
        log.info("first name is")
        signInpage.getPassword().send_keys("password")
        signInpage.clickSignInButton()

        alertText = signInpage.getErrorMessage().text
        log.info("Text received from application is " + alertText)
        assert ("failed" in alertText)
        
        
        #self.driver.refresh()

    # #@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    # def getData(self, request):
    #     return request.param
