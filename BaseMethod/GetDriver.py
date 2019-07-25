import os

from appium import webdriver


class GetDriver:
    def __init__(self):
        self.desired = None

    def get_driver(self, app_package, app_activity):
        self.desired ={}
        self.desired['platformName'] = 'Android'
        self.desired['platformVersion'] = '8.0.0'
        self.desired['deviceName'] = 'HUAWEI nova2'
        self.desired['appPackage'] = app_package
        self.desired['appActivity'] = app_activity
        self.desired['unicodeKeyboard'] = True
        self.desired['resetKeyboard'] = True
        return webdriver.Remote('http://localhost:4723/wd/hub', self.desired)