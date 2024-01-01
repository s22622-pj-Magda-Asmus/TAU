from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

@given('User is on the treenuts.pl website')
def step_impl_given(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get('https://treenuts.pl/')

@when('User hovers over {menu} and selects {submenu}')
def step_impl_when(context, menu, submenu):
    sklep = context.driver.find_element(By.XPATH, '//*[@id="menu-item-16527"]/a')
    actions = ActionChains(context.driver)
    actions.move_to_element(sklep).perform()
    time.sleep(2)
    submenu_element = context.driver.find_element(By.XPATH, f'//*[@id="menu-item-62040"]/a')
    submenu_element.click()

@then('User selects a specific cream and adds it to the basket')
def step_impl_then(context):
    cream = context.driver.find_element(By.XPATH, '//*[@id="main"]/div/ul/li[2]/a[1]/h2')
    cream.click()
    addToBasketButton = context.driver.find_element(By.XPATH, '//*[@id="product-31231"]/div[1]/div[2]/div/div[1]/form/div/div/div[3]/button')
    addToBasketButton.click()
    time.sleep(2)
    goToBasket = context.driver.find_element(By.XPATH, '//*[@id="navbar-basket-count"]/a/span[1]')
    goToBasket.click()

@then('User verifies the basket value is {expected_value}')
def step_impl_then(context, expected_value):
    basketValue = context.driver.find_element(By.XPATH, '//*[@id="post-2192"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span/bdi')
    basket = basketValue.text
    assert basket == "46,99 zł"

    context.driver.quit()
