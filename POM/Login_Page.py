from selenium.webdriver.common.by import By
from POM.Base import Base


class LoginPage(Base):
    username = (By.ID, 'txtUsername')
    password = (By.ID, 'txtPassword')
    submit_button = (By.CSS_SELECTOR, 'button[type = "submit"]')

    def login(self, user_name, pass_word):
        self.wait_element(*self.username)
        self.send_keys(*self.username, user_name)
        self.send_keys(*self.password, pass_word)
        self.click_element(*self.submit_button)

    def verify_login(self):
        title = self.driver.title
        if title == 'Employee Management':
            return True
        else:
            return False
