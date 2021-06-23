from selenium.webdriver.common.by import By


class ManagerPage:
    def __init__(self, driver):
        self.driver = driver

    uid = (By.CSS_SELECTOR, "input[name='uid']")
    paswd = (By.CSS_SELECTOR, "input[name='password']")
    loginbut = (By.CSS_SELECTOR, "input[name='btnLogin']")
    clickchangepasslink = (By.XPATH, "//a[contains(text(),'Change Password')]")
    opass = (By.XPATH, "//input[@name='oldpassword']")
    npass = (By.XPATH, "//input[@name='newpassword']")
    cpass = (By.XPATH, "//input[@name='confirmpassword']")
    submit = (By.XPATH, "// input[ @ name = 'sub']")

    def getUserID(self):
        return self.driver.find_element(*ManagerPage.uid)

    def getPaswd(self):
        return self.driver.find_element(*ManagerPage.paswd)

    def getLoginBut(self):
        return self.driver.find_element(*ManagerPage.loginbut)

    def getChangePass(self):
        return self.driver.find_element(*ManagerPage.clickchangepasslink)

    def getOldPass(self):
        return self.driver.find_element(*ManagerPage.opass)

    def getNewPass(self):
        return self.driver.find_element(*ManagerPage.npass)

    def getConfirmPass(self):
        return self.driver.find_element(*ManagerPage.cpass)

    def getSubmitBut(self):
        return self.driver.find_element(*ManagerPage.submit)
