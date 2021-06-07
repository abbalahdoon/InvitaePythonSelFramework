
import pytest
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.AuthenticationPage import AuthenticationPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.PaymentPage import PaymentPage

from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.ShippingPage import ShippingPage
from pageObjects.SummaryPage import SummaryPage
from utilities.BaseClass import BaseClass


class TestCartPage(BaseClass):
    def test_AddToCart(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        homepage = HomePage(self.driver)
        homepage.clickSignInButtonHP()
        authenticationpage.getEmail().send_keys("tugbaozden@gmail.com")
        authenticationpage.getPassword().send_keys("12345")
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
        time.sleep(2)
        assert "7" in summarypage.getProductAmount().text
        assert "198.38" in summarypage.getTotalPrice().text
        log.info("User is able to add items to cart. Item amount and total price are calculated successfully")

    def test_RemoveCart(self):
        log = self.getLogger()
        summarypage = SummaryPage(self.driver)

        print(summarypage.getDeletedAmount().text)

        deletedAmount = summarypage.getDeletedAmount().text
        delAmount = float(deletedAmount[-5:])
        print(delAmount)
        summarypage.getProductDeleted()
        newTotPrice = float(198.38 - delAmount)
        newTotalPriceString = str(newTotPrice)
        print(newTotPrice)
        time.sleep(2)
        assert "6" in summarypage.getProductAmount().text
        assert newTotalPriceString in summarypage.getTotalPrice().text
        log.info("User is able to remove items from cart. Item amount and total price are calculated successfully")