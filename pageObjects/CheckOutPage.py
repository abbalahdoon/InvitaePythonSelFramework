from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class ShippingPage:

    def __init__(self, driver):
        self.driver = driver


    termsCheckBox = (By.ID, "#cgv")


    def getTermsCheckbox(self):
         self.driver.find_elements(*ShippingPage.termsCheckBox).click()



