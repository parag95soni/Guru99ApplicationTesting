import time

from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
    # self.driver.find_element_by_css_selector("input[name='password']").send_keys("ArugUsU")
    # self.driver.find_element_by_css_selector("input[name='uid']").send_keys("mngr333840")
    # self.driver.find_element_by_css_selector("input[name='btnLogin']").click()
    uid = (By.CSS_SELECTOR, "input[name='uid']")
    paswd = (By.CSS_SELECTOR, "input[name='password']")
    loginbut = (By.CSS_SELECTOR, "input[name='btnLogin']")
    mangerid = (By.XPATH, "//tr[@class='heading3']/td")


    def getUserID(self):
        return self.driver.find_element(*LoginPage.uid)

    def getPaswd(self):
        return self.driver.find_element(*LoginPage.paswd)

    def getLoginBut(self):
        return self.driver.find_element(*LoginPage.loginbut)

