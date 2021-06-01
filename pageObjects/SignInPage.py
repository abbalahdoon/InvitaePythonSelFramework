from selenium.webdriver.common.by import By


class SignInPage:

    def __init__(self, driver):
        self.driver = driver


    loginButton = (By.CSS_SELECTOR, "a.login")
    inputEmail = (By.ID, "email")
    inputPassword = (By.ID, "passwd")
    errorMessage = (By.XPATH, "(//div[@class='alert alert-danger']/ol/li)[1]")
    signInButton = (By.ID, "SubmitLogin")


    def gotoSignInPage(self):
        self.driver.find_element(*SignInPage.loginButton).click()

    def getEmail(self):
        return self.driver.find_element(*SignInPage.inputEmail)

    def getPassword(self):
        return self.driver.find_element(*SignInPage.inputPassword)

    def clickSignInButton(self):
        self.driver.find_element(*SignInPage.signInButton).click()

    def getErrorMessage(self):
        return self.driver.find_element(*SignInPage.errorMessage)


