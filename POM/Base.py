from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, context):
        self.driver = context.driver

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator, element):
        try:
            item = self.driver.find_element(locator, element)
            return item
        except NoSuchElementException:
            return None

    def wait_element(self, locator, element):
        try:
            item = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((locator, element)))
            return item
        except TimeoutException:
            return None

    def click_element(self, locator, element):
        try:
            item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator, element)))
            item.click()
        except ElementNotInteractableException:
            item = self.driver.find_element(locator, element)
            ActionChains(self.driver).move_to_element(item).click().perform()

    def send_keys(self, locator, element, value):
        try:
            item = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator, element)))
            item.send_keys(value)
        except ElementNotInteractableException:
            item = self.driver.find_element(locator, element)
            ActionChains(self.driver).move_to_element(item).click().send_keys(value).perform()
