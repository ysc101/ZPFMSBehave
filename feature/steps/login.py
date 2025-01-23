from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
@given(u'Launch Browser')
def step_impl(context):
    @given(u'User is on Home Page')
    def launch_browser(context):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--ignore-certificate-errors")
        context.driver = webdriver.Chrome(options=options)

@when(u'User navigates to ZPFMS login Page')
def step_impl(context):
            raise NotImplementedError(u'STEP: When User navigates to ZPFMS login Page')



@then(u'User enters "<username>" and "<password>"')
def step_impl(context):
        raise NotImplementedError(u'STEP: Then User enters "<username>" and "<password>"')

def Enter_Username_Password(context):
        username = "MAKERWORK"  # Replace with actual test data
        password = "Pass@123"  # Replace with actual test data

        context.driver.find_element(By.ID, "txtUser").send_keys(username)
        context.driver.find_element(By.ID, "txtPass").send_keys(password)
        context.driver.find_element(By.ID, "btnLogin").click()

@then(u'User should get logged in')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User enters "<username>" and "<password>"')


@then(u'Message displayed Login Successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Message displayed Login Successfully')





