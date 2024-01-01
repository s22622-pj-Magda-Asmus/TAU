from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('User is on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://www.saucedemo.com/')
    title = context.driver.title
    assert "Swag Labs" in title

@when('User enters valid credentials')
def step_impl(context):
    wait = WebDriverWait(context.driver, 10)
    user_name_field = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
    user_name_field.click()
    user_name_field.send_keys("standard_user")
    time.sleep(2)
    password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
    password_field.click()
    password_field.send_keys("secret_sauce")
    time.sleep(2)
    button_login = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
    button_login.click()
    time.sleep(2)

@then('User should be redirected to the inventory page')
def step_impl(context):
    current_url = context.driver.current_url
    assert current_url == "https://www.saucedemo.com/inventory.html", "URL is not as expected"
    context.driver.quit()
