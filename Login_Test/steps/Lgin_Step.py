from behave import *
from POM.Base import Base
from POM.MyDriver import MyDriver
from POM.Login_Page import LoginPage


@given('Open a browser and navigate to "{url}"')
def navigate_to_url(context, url):
    context.driver = MyDriver().chrome_driver()
    Base(context).navigate_to(url)


@when('Enter Valid Credentials: "{username}" and "{password}".')
def perform_login(context, username, password):
    LoginPage(context).login(username,password)


@then('Login should be successful')
def verify_login(context):
    status = LoginPage(context).verify_login()
    assert status is True, 'Login Failed.'
