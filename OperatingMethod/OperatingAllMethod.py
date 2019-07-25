import allure
from BaseMethod.BaseMethod import BaseMethod
from PageElement import Register


class OperatingAllMethod(BaseMethod):

    def __init__(self, driver):
        BaseMethod.__init__(self, driver)

    @allure.step(title='点击进入爱优品按钮')
    def click_info_ayp_button(self):
        self.click_element(Register.ayp_button)

    @allure.step(title='点击始终允许按钮')
    def click_allow_button(self):
        self.click_element(Register.allow_button)

    @allure.step(title='点击我的按钮')
    def click_my_button(self):
        self.click_element(Register.my_button)

    @allure.step(title='点击马上登录按钮')
    def click_register_login_button(self):
        self.click_element(Register.register_login)

    @allure.step(title='点击登录按钮')
    def click_register_button(self):
        self.click_element(Register.register_button)

    @allure.step(title='点击设置按钮')
    def click_setting_button(self, i):
        self.click_element(Register.setting_button[i])

    @allure.step(title='点击退出登录按钮')
    def click_quit_register_button(self):
        self.click_element(Register.quit_register_button)

    @allure.step(title='点击弹窗中确定按钮')
    def click_confirm_button(self):
        self.click_element(Register.confirm_button)

    @allure.step(title='点击我发布的按钮')
    def click_my_issue_button(self):
        self.click_element(Register.my_issue_button)

