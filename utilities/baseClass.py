import inspect
import logging

import pytest


@pytest.mark.usefixtures("browserInvoke")
class BaseClass:
    def getLog(self):
        logname = inspect.stack()[1][3]
        logger = logging.getLogger(logname)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def alert(self,alertmsg):
        assert self.driver.switch_to.alert.text == alertmsg
        self.driver.switch_to.alert.accept()

