from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver


    searchBox = (By.ID, "search_query_top")
    searchSubmitButton = (By.XPATH, "//button[@name='submit_search']")
    errorMessageNoSearchResult = (By.CSS_SELECTOR, "p.alert.alert-warning")

    items = (By.XPATH, "//div[@class='right-block']/h5/a")
    addToCartButton = (By.XPATH, "//a[@title='Add to cart']")
    continueShoppingButton = (By.XPATH, "//span[@title='Continue shopping']")
    proceedCheckoutButton = (By.XPATH, "//span[contains(text(), 'Proceed to checkout')]")

    gridView = (By.XPATH, "//a[@title='Grid']")
    listView = (By.XPATH, "//a[@title='List']/i")
    listSelected = (By.XPATH, "//li[@id='list']")
    gridSelected = (By.XPATH, "//li[@id='grid']")
    cartButton = (By.XPATH, "//div[@class='shopping_cart']")

    def getSearchBox(self):
        return self.driver.find_element(*SearchPage.searchBox)

    def submitSearch(self):
        self.driver.find_element(*SearchPage.searchSubmitButton).click()

    def getSearchResult(self):
        return self.driver.find_element(*SearchPage.errorMessageNoSearchResult)

    def getItems(self):
        return self.driver.find_elements(*SearchPage.items)

    def AddToCart(self):
        return self.driver.find_elements(*SearchPage.addToCartButton)

    def getContinueShopping(self):
        self.driver.find_element(*SearchPage.continueShoppingButton).click()

    def getProceedToCheckout(self):
        self.driver.find_element(*SearchPage.proceedCheckoutButton).click()
    def ProceedToCheckOutButton(self):
        return self.driver.find_element(*SearchPage.proceedCheckoutButton)

    def getGridView(self):
        return self.driver.find_element(*SearchPage.gridView)

    def getListView(self):
        return self.driver.find_element(*SearchPage.listView)
    def getListSelected(self):
        return self.driver.find_element(*SearchPage.listSelected)
    def getGridSelected(self):
        return self.driver.find_element(*SearchPage.gridSelected)

    def getCart(self):
         self.driver.find_element(*SearchPage.cartButton).click()


