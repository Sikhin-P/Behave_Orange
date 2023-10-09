from selenium import webdriver


class MyDriver:

    def __init__(self):
        self.driver = None

    def chrome_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver
