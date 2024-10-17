import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from amazoncaptcha import AmazonCaptcha
from utilities.baseClass import BaseClass
from pageObjects.homePage import HomePage


class TestSearch(BaseClass):

    def test_search(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        captcha = AmazonCaptcha.fromdriver(self.driver)
        solution = captcha.solve()

        self.verifyVisibility(homePage.getCaptchaBox())
        homePage.getCaptchaBox().send_keys(solution)
        homePage.getCaptchaBtn().click()

        self.verifyVisibility(homePage.getSearch())
        homePage.getSearch().send_keys("nasa anniversary")
        homePage.getSearchBtn().click()

        time.sleep(10)