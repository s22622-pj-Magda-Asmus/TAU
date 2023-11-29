from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestMyWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = None

    def tearDown(self):
        # Kod wykonywany po każdym teście
        if self.driver:
            self.driver.quit()

    def test_login(self):
        browsers_to_test = [
            ('Chrome', webdriver.Chrome),
            ('Firefox', webdriver.Firefox)
        ]

        for browser_name, browser in browsers_to_test:
            with self.subTest(browser_name=browser_name):
                self.driver = browser()
                self.driver.maximize_window()
                self.driver.implicitly_wait(10)

                self.driver.get('https://www.saucedemo.com/')
                title = self.driver.title
                self.assertEqual("Swag Labs", title)

                wait = WebDriverWait(self.driver, 10)
                user_name_field = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
                user_name_field.click()
                user_name_field.send_keys("standard_user")
                time.sleep(6)
                password_field = wait.until(EC.presence_of_element_located((By.ID, 'password')))
                password_field.click()
                password_field.send_keys("secret_sauce")
                time.sleep(6)
                button_login = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
                button_login.click()
                time.sleep(6)
                current_url = self.driver.current_url
                self.assertEqual("https://www.saucedemo.com/inventory.html", current_url, "URL nie jest zgodny z oczekiwanym")

                self.driver.quit()

if __name__ == "__main__":
    unittest.main()