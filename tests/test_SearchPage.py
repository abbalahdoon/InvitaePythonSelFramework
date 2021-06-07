from pageObjects.SearchPage import SearchPage

from selenium import webdriver
import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AuthenticationPage import AuthenticationPage
from utilities.BaseClass import BaseClass


class TestSearchPage(BaseClass):

    #Verify when user search an item with no results, user is notified with 'no result' message
    def test_SearchWithNoResults(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.getSearchBox().send_keys("glass")
        searchpage.submitSearch()
        self.verifyElementPresence("css", "p.alert.alert-warning")
        searchResultMessage = searchpage.getSearchResult().text
        log.info("User is able to view no result message successfully. Search result message is :  " + searchResultMessage)
        assert ("No results" in searchResultMessage)
        self.driver.back()

    # Verify that user is able to view the items in list view mode
    def test_ListView(self):
        log = self.getLogger()
        authenticationpage = AuthenticationPage(self.driver)
        searchpage = SearchPage(self.driver)
        searchpage.getSearchBox().send_keys("dress")
        searchpage.submitSearch()
        searchpage.getListView().click()
        assert searchpage.getListSelected().get_attribute("class") == "selected"
        log.info("User is able to view items in list mode successfully")
        self.driver.back()

    #Verify that user is able to view the items in grid view mode
    def test_GridView(self):
        log = self.getLogger()
        searchpage = SearchPage(self.driver)
        searchpage.getSearchBox().send_keys("dress")
        searchpage.submitSearch()
        searchpage.getListView().click()
        searchpage.getGridView().click()
        assert searchpage.getGridSelected().get_attribute("class") == "selected"
        log.info("User is able to view items in grid mode successfully")










