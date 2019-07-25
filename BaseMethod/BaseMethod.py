from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
import allure, time


class BaseMethod:

    def __init__(self, driver):
        self.driver = driver
        self.element = None

    def find_element(self, loc, timeout=15, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=15, poll=1):
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        self.element = self.find_element(loc)
        self.element.click()

    @allure.step(title="输入操作")
    def send_keys_text(self, loc, text, operation):
        self.element = self.find_element(loc)
        self.element.clear()
        allure.attach(operation, "{0}".format(text))
        self.element.send_keys(text)

    @allure.step(title="截图操作")
    def gain_screenshot(self, file_name):
        self.time = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(time.time()))
        allure.attach("图片名字", "{0}".format("app_%s.png" % self.time))
        self.path = "C:/Users/Administrator/PycharmProjects/PythonToAppTestScriptCode/GainScreenshot/" + file_name + "_%s.png"
        return self.driver.get_screenshot_as_file(self.path % self.time)