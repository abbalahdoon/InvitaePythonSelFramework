import pytest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from TestData.AuthenticationPageData import AuthenticationPageData
from pageObjects.AuthenticationPage import AuthenticationPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.PaymentPage import PaymentPage

from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.ShippingPage import ShippingPage
from pageObjects.SummaryPage import SummaryPage
from utilities.BaseClass import BaseClass


class TestEndToEnd(BaseClass):

    def test_e2e(self, getData):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmail().send_keys(getData["emailaddress"])
        authenticationpage.getPassword().send_keys(getData["password"])
        self.verifyElementPresence("id", "SubmitLogin")
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", authenticationpage.getSignInButton())
        authenticationpage.clickSignInButton()

        searchpage = SearchPage(self.driver)
        searchpage.getSearchBox().send_keys("dress")
        searchpage.submitSearch()
        searchpage.getListView().click()
        buttons = searchpage.AddToCart()
        for button in buttons:
            button.click()
        time.sleep(2)
        searchpage.getProceedToCheckout()

        summarypage = SummaryPage(self.driver)

        assert "7" in summarypage.getProductAmount().text
        assert "198.38" in summarypage.getTotalPrice().text
        time.sleep(2)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);",
                                   summarypage.getProceedToCheckOutButton())
        summarypage.clickProceedToChechOutButton()
        time.sleep(2)
        self.driver.execute_script("return arguments[0].scrollIntoView(true);",
                                   summarypage.getProceedToCheckOutButton())
        summarypage.clickProceedToChechOutButton()

        shippingpage = ShippingPage(self.driver)

        self.driver.execute_script("return arguments[0].scrollIntoView(true);", shippingpage.getTermsCheckbox())
        shippingpage.clickTermsCheckbox()
        self.driver.execute_script("return arguments[0].scrollIntoView(true);",
                                   summarypage.getProceedToCheckOutButton())
        summarypage.clickProceedToChechOutButton()
        time.sleep(2)
        paymentpage = PaymentPage(self.driver)
        paymentpage.getPayByCheckButton()
        paymentpage.getConfirmMyOrder()
        confirmpage = ConfirmPage(self.driver)
        confirmation = confirmpage.getConfirmationText().text
        assert "complete" in confirmation
        log.info("User completed checkout process,successfully submitted order")


    @pytest.fixture(params=AuthenticationPageData.test_AuthenticationPage_data)
    def getData(self, request):
     return request.param