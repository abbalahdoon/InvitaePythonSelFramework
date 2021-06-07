from selenium.webdriver.common.by import By


class AuthenticationPage:

    def __init__(self, driver):
        self.driver = driver


    loginButton = (By.CSS_SELECTOR, "a.login")
    inputEmail = (By.ID, "email")
    inputPassword = (By.ID, "passwd")
    errorMessageInvalidCredentials = (By.XPATH, "(//div[@class='alert alert-danger']/ol/li)[1]")
    signInButton = (By.ID, "SubmitLogin")

    inputEmailCreateAccount = (By.ID, "email_create")
    errorMessageAlreadyRegistered = (By.XPATH, "//div[@id='create_account_error']//li")
    createAccountButton = (By.ID, "SubmitCreate")

    welcomeMessage = (By.CSS_SELECTOR, 'p.info-account')

    signOutButton = (By.CSS_SELECTOR, 'a.logout')
    loginButtonText = (By.LINK_TEXT, "a.login")

    def getLogin(self):
        return self.driver.find_element(*AuthenticationPage.loginButton)

    def goToAuthenticationPage(self):
        self.driver.find_element(*AuthenticationPage.loginButton).click()

    def getEmail(self):
        return self.driver.find_element(*AuthenticationPage.inputEmail)

    def getPassword(self):
        return self.driver.find_element(*AuthenticationPage.inputPassword)

    def clickSignInButton(self):
        self.driver.find_element(*AuthenticationPage.signInButton).click()

    def getErrorMessage(self):
        return self.driver.find_element(*AuthenticationPage.errorMessageInvalidCredentials)

    def getEmailCreateAccount(self):
        return self.driver.find_element(*AuthenticationPage.inputEmailCreateAccount)

    def clickCreateAccountButton(self):
        self.driver.find_element(*AuthenticationPage.createAccountButton).click()

    def getErrorMessageAlreadyRegistered(self):
        return self.driver.find_element(*AuthenticationPage.errorMessageAlreadyRegistered)

    def getWelcomeMessage(self):
        return self.driver.find_element(*AuthenticationPage.welcomeMessage)

    def clickSignOutButton(self):
        self.driver.find_element(*AuthenticationPage.signOutButton).click()

    def getSignInButton(self):
        return self.driver.find_element(*AuthenticationPage.signInButton)


