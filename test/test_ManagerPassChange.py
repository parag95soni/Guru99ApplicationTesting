import pytest

from Test_Data.ManagerPageData import ManagerPageData
from pageObject.ManagerPage import ManagerPage
from utilities.baseClass import BaseClass


class TestManagerPage(BaseClass):
    def test_ChangePass(self,getData):
        managerpage = ManagerPage(self.driver)
        managerpage.getUserID().send_keys(getData["userid"])
        managerpage.getPaswd().send_keys(getData["password"])
        managerpage.getLoginBut().click()
        managerpage.getChangePass().click()
        managerpage.getOldPass().send_keys(getData["opass"])
        managerpage.getNewPass().send_keys(getData["npass"])
        managerpage.getConfirmPass().send_keys(getData["cpass"])
        managerpage.getSubmitBut().click()
        self.alert("Old Password is incorrect")

    @pytest.fixture(params=ManagerPageData.test_mdata)
    def getData(self,request):
        return request.param