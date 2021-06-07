from selenium.webdriver.common.by import By


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver

    paybycheckButton = (By.CSS_SELECTOR, "a.cheque")
    confirmMyOrderButton = (By.XPATH, "//span[contains(text(), 'I confirm my order')]")

    def getPayByCheckButton(self):
        self.driver.find_element(*PaymentPage.paybycheckButton).click()

    def getConfirmMyOrder(self):
        self.driver.find_element(*PaymentPage.confirmMyOrderButton).click()
