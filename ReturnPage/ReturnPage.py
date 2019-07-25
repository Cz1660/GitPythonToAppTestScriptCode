from OperatingMethod.OperatingAllMethod import OperatingAllMethod


class ReturnPage:

    def __init__(self, driver):
        self.driver = driver

    def return_page(self):
        return OperatingAllMethod(self.driver)