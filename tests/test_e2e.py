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
from pageObjects.CheckOutPage import CheckOutPage, ShippingPage
from pageObjects.HomePage import HomePage
from pageObjects.SearchPage import SearchPage
from pageObjects.SummaryPage import SummaryPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
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

        assert "7" in summarypage.getProductAmount().text
        assert "198.38"in summarypage.getTotalPrice().text

        searchpage.getProceedToCheckout()
        searchpage.getProceedToCheckout()
        shippingpage = ShippingPage(self.driver)
        self.verifyElementPresence("id", "#cgv")
        shippingpage.getTermsCheckbox()
        searchpage.getProceedToCheckout()
        searchpage.getProceedToCheckout()
        paymentpage = PaymentPage(self.driver)
        paymentpage.paybycheckButton()

        paymentpage.confirmMyOrderButton

        confirmpage = ConfirmPage(self.driver)
        confirmationText = confirmpage.getConfirmationText().Text

        assert "complete" in confirmationText












        # time.sleep(3)
        # print(summarypage.getDeletedAmount().text)
        #
        # totalPrice = summarypage.getProductAmount().text
        # deletedAmount = summarypage.getProductDeleted()
        # #
        #
        # #
        # #print(summarypage.getTotalPrice().text)
        #
        # #
        #
        # #int newAmount = totalPrice - deletedAmount
        # #
        # time.sleep(2)
        # assert "6" in summarypage.getProductAmount().text
        # assert "147.39" in summarypage.getTotalPrice().text
        # #
        # # searchpage.getProceedToCheckout()



























        # action = ActionChains(self.driver)
        # items = []
        # print(len(searchpage.getItems()))
        # i = -1
        # count = 0
        # items = searchpage.getItems()
        # for item in items:
        #     i = i+1
        #     action.move_to_element(item).perform()
        #     itemText = item.text
        #     time.sleep(5)
        #     if "Dress" in itemText:
        #         action.move_to_element(searchpage.AddToCart()[i]).click().pause(2).perform()
        #         searchpage.getContinueShopping()
        #         time.sleep(5)
        # searchpage.getProceedToCheckout()









