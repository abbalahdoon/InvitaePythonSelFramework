
from selenium.webdriver.common.by import By
class SummaryPage:

    def __init__(self, driver):
        self.driver = driver

    productAmount = (By.ID, "summary_products_quantity" )
    totalPrice = (By.ID, "total_price")
    deleteButton = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[7]/div[1]/a[1]/i[1]")
    deletedAmount = (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/table[1]/tbody[1]/tr[1]/td[6]/span[1]")
    proceedToCheckoutButton = (By.XPATH, "(//span[contains(text(), 'Proceed to checkout')])[2]")

    def getProductAmount(self):
        return self.driver.find_element(*SummaryPage.productAmount)

    def getTotalPrice(self):
        return self.driver.find_element(*SummaryPage.totalPrice)

    def getProductDeleted(self):
        self.driver.find_element(*SummaryPage.deleteButton).click()

    def getDeletedAmount(self):
        return self.driver.find_element(*SummaryPage.deletedAmount)

    def getProceedToCheckOutButton(self):
        return self.driver.find_element(*SummaryPage.proceedToCheckoutButton)

    def clickProceedToChechOutButton(self):
        self.driver.find_element(*SummaryPage.proceedToCheckoutButton).click()


