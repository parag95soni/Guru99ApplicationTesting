import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from utilities.baseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
    # self.driver.find_element_by_css_selector("input[name='password']").send_keys("ArugUsU")
    # self.driver.find_element_by_css_selector("input[name='uid']").send_keys("mngr333840")
    # self.driver.find_element_by_css_selector("input[name='btnLogin']").click()
    uid = (By.CSS_SELECTOR, "input[name='uid']")
    paswd = (By.CSS_SELECTOR, "input[name='password']")
    loginbut = (By.CSS_SELECTOR, "input[name='btnLogin']")


    def getUserID(self):
        return self.driver.find_element(*LoginPage.uid)

    def getPaswd(self):
        return self.driver.find_element(*LoginPage.paswd)

    def getLoginBut(self):
        return self.driver.find_element(*LoginPage.loginbut)

    def getValidation(self):
        log = self.getLog()
        try:
            alert = Alert(self.driver)
            assert "User or Password is not valid" == alert.text
            log.info(alert.text)
            alert.accept()
        except NoAlertPresentException:
            assert "Guru99 Bank Manager HomePage" == self.driver.title
            log.info(self.driver.title)