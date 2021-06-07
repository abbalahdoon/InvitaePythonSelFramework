from selenium.webdriver.common.by import By

from pageObjects.AuthenticationPage import AuthenticationPage



class HomePage:

    def __init__(self, driver):
        self.driver = driver



    signInHPButton = (By.CSS_SELECTOR, "a.login")

    def clickSignInButtonHP(self):
        self.driver.find_element(*HomePage.signInHPButton).click()
        authenticationpage = AuthenticationPage(self.driver)
        return AuthenticationPage






