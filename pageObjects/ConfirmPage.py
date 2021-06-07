from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    confirmationText = (By.CSS_SELECTOR, "p.alert.alert-success")

    def getConfirmationText(self):
        return self.driver.find_element(*ConfirmPage.confirmationText)
