import time, pytest, allure
import TestUseCaseAppToAiYouPing
from BaseMethod.GetDriver import GetDriver
from ReturnPage.ReturnPage import ReturnPage
from PageElement import Register
from Yaml.ReadYaml import ReadYaml


def gain_yaml():
    yaml_data_list = []
    yaml_data = ReadYaml("InputYaml.yaml").read_yaml()
    for i in yaml_data.keys():
        yaml_data_list.append((i,yaml_data.get(i).get("username"), yaml_data.get(i).get("password"), yaml_data.get(i).
                               get("initem_un"), yaml_data.get(i).get("initem_pd"), yaml_data.get(i).get("tag"),
                               yaml_data.get(i).get("assert_username"), yaml_data.get(i).get("immediately_register")))
    return yaml_data_list


class TestAppToLogin:
    # 启动app
    def setup_class(self):
        self.Dv = ReturnPage(GetDriver().get_driver(TestUseCaseAppToAiYouPing.app_package, TestUseCaseAppToAiYouPing.
                                                    app_activity))
        time.sleep(2)
        for i in range(3):
            # 屏幕向左滑动
            self.Dv.driver.swipe(1051, 921, 26, 928, 0)
            time.sleep(0.3)
        # 点击进入爱优品
        self.Dv.return_page().click_info_ayp_button()
        time.sleep(1)
        # 点击始终允许
        self.Dv.return_page().click_allow_button()
        time.sleep(1)
        # 点击我的按钮
        self.Dv.driver.tap([(943, 1866), (1001, 1905)], 0)

    # 关闭app
    def teardown_class(self):
        self.Dv.driver.quit()

    # 多个用例集order=1
    @pytest.mark.run(order=1)
    # 利用参数化实现多个用例（账号登录操作）
    @pytest.mark.parametrize('test_number, username, password, initem_un, initem_pd, tag, assert_username, '
                             'immediately_register', gain_yaml())
    def test_register(self, test_number, username, password, initem_un, initem_pd, tag, assert_username,
                      immediately_register):
        allure.attach("用例编号", "{0}".format(test_number))
        time.sleep(1)
        try:
            # 点击马上登录
            self.Dv.driver.tap([(276, 257), (969, 325)], 0)
            time.sleep(1)
            assert self.Dv.return_page().find_element(Register.register_button)
            # 输入账号
            self.Dv.return_page().send_keys_text(Register.input_phone, username, initem_un)
            # 输入密码
            self.Dv.return_page().send_keys_text(Register.input_password, password, initem_pd)
            # 点击登录
            self.Dv.return_page().click_register_button()
            time.sleep(1)
            try:
                if tag == '0':
                    time.sleep(0.2)
                    for i in range(2):
                        # 屏幕向上滑动
                        self.Dv.driver.swipe(10, 1666, 10, 99, 0)
                    time.sleep(0.5)
                    # 点击设置按钮
                    self.Dv.driver.tap([(45, 1654), (123, 1732)], 0)
                    time.sleep(0.3)
                    # 点击退出登录
                    self.Dv.return_page().click_quit_register_button()
                    time.sleep(0.2)
                    # 点击确定退出当前登录弹窗中确定按钮
                    self.Dv.return_page().click_confirm_button()
                    time.sleep(0.2)
                    try:
                        for i in range(2):
                            # 屏幕向下滑动
                            self.Dv.driver.swipe(10, 99, 10, 1666, 0)
                        # 退出成功，未找到登录按钮
                        assert self.Dv.return_page().find_element(Register.my_issue_button)
                        # 获取当前页面的截图
                        self.Dv.return_page().gain_screenshot(test_number + '注销成功')
                    except Exception as e:
                        # 获取当前页面的截图
                        self.Dv.return_page().gain_screenshot(test_number + '注销失败')
                if tag == '1':
                    self.Dv.return_page().gain_screenshot(test_number + '登录失败')
            except Exception as e:
                # 获取当前页面的截图
                self.Dv.return_page().gain_screenshot(test_number + '异常')
        except Exception as e:
            # 获取当前页面的截图
            self.Dv.return_page().gain_screenshot(test_number + '大异常')



