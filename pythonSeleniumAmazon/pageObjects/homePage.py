from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    searchBar = (By.CSS_SELECTOR, "#twotabsearchtextbox")
    searchBtn = (By.CSS_SELECTOR, "#nav-search-submit-button")
    captchaBox = (By.XPATH, "(//input[@id='captchacharacters'])[1]")
    captchaBtn = (By.XPATH, "//button[normalize-space()='Continue shopping']")

    def getSearch(self):
        return self.driver.find_element(*HomePage.searchBar)

    def getSearchBtn(self):
        return self.driver.find_element(*HomePage.searchBtn)

    def getCaptchaBox(self):
        return self.driver.find_element(*HomePage.captchaBox)

    def getCaptchaBtn(self):
        return self.driver.find_element(*HomePage.captchaBtn)