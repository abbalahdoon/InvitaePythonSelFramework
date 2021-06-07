from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class ShippingPage:

    def __init__(self, driver):
        self.driver = driver


    termsCheckBox = (By.XPATH, "//input[@type='checkbox']")


    def clickTermsCheckbox(self):
         self.driver.find_element(*ShippingPage.termsCheckBox).click()

    def getTermsCheckbox(self):
        return self.driver.find_element(*ShippingPage.termsCheckBox)


