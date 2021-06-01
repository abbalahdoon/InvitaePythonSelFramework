from selenium.webdriver.common.by import By


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver


    loginButton = (By.CSS_SELECTOR, "a.login")
    inputEmail = (By.ID, "email_create")
    inputPassword = (By.ID, "passwd")
    errorMessage = (By.XPATH, "//div[@id='create_account_error']//li")
    createAccountButton = (By.ID, "SubmitCreate")



    # def gotoSignInPage(self):
    #     self.driver.find_element(*CreateAccountPage.loginButton).click()
    def getEmail(self):
        return self.driver.find_element(*CreateAccountPage.inputEmail)

    def clickCreateAccountButton(self):
        self.driver.find_element(*CreateAccountPage.createAccountButton).click()

    def getErrorMessage(self):
        return self.driver.find_element(*CreateAccountPage.errorMessage)