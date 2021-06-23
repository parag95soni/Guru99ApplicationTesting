import pytest
from selenium.common.exceptions import NoAlertPresentException

from Test_Data.LoginPageData import LoginPageData
from pageObject.LoginPage import LoginPage
from utilities.baseClass import BaseClass


class TestLoginPage(BaseClass):
    def test_ValidLogin(self,getData):
        log = self.getLog()
        loginpage = LoginPage(self.driver)
        loginpage.getUserID().send_keys(getData["userid"])
        log.info("User ID Used to Login "+ getData["userid"])
        loginpage.getPaswd().send_keys(getData["password"])
        log.info("Password Used to Login " + getData["password"])
        loginpage.getLoginBut().click()
        try:
            self.alert("User or Password is not valid")
        except NoAlertPresentException:
            assert "mngr333840" in self.driver.find_element(*LoginPage.mangerid).text
            self.driver.get_screenshot_as_file("ManagerID.png")




    @pytest.fixture(params=LoginPageData.test_logindata)
    def getData(self, request):
        return request.param