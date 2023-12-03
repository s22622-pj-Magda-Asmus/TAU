from selenium import webdriver
import unittest
import time
import logging
from selenium.webdriver.common.action_chains import ActionChains



class TestMyWebsite(unittest.TestCase):

    def setUp(self):
        self.driver=None


    def tearDown(self):
        # Kod wykonywany po każdym teście
        if self.driver:
            self.driver.quit()

    def test_title(self):
        browsers_to_test = [
            ('Chrome', webdriver.Chrome),
            ('Firefox', webdriver.Firefox)
        ]

        for browser_name, browser in browsers_to_test:
            with self.subTest(browser_name=browser_name):
                self.driver = browser()
                self.driver.maximize_window()  # Maksymalizacja okna przeglądarki
                self.driver.implicitly_wait(10)

                self.driver.get('https://treenuts.pl/')
                title = self.driver.title
                self.assertEqual("Tree Nuts – Orzechy laskowe z polskich sadów", title)  # Zmodyfikuj oczekiwany tytuł

                self.driver.quit()

    def test_addingToBasket(self):
        browsers_to_test = [
            ('Chrome', webdriver.Chrome),
            ('Firefox', webdriver.Firefox)
        ]

        for browser_name, browser in browsers_to_test:
            with self.subTest(browser_name=browser_name):
                self.driver = browser()
                self.driver.maximize_window()  # Maksymalizacja okna przeglądarki
                self.driver.implicitly_wait(10)

                self.driver.get('https://treenuts.pl/')
                sklep = self.driver.find_element(by='xpath', value='//*[@id="menu-item-16527"]/a')
                actions = ActionChains(self.driver)

                # Najechanie myszką na element "Sklep"
                actions.move_to_element(sklep).perform()
                time.sleep(2)

                #wybranie oferty z kremami
                creams = self.driver.find_element(by='xpath', value='//*[@id="menu-item-62040"]/a')
                creams.click()
                logging.warning('Poprawne przejscie do podstrony z kremami')

                #wybranie konkretnego kremu
                cream = self.driver.find_element(by='xpath', value='//*[@id="main"]/div/ul/li[2]/a[1]/h2')
                cream.click()
                #dodanie go do koszyka
                addToBasketButton= self.driver.find_element(by='xpath', value='//*[@id="product-31231"]/div[1]/div[2]/div/div[1]/form/div/div/div[3]/button')
                addToBasketButton.click()
                logging.warning('Krem został dodany do koszyka zakupowego')

                #sprawdzenie czy wartość koszyka sie zgadza
                goToBasket = self.driver.find_element(by='xpath', value='// *[ @ id = "navbar-basket-count"] / a / span[1]')
                goToBasket.click()
                basketValue = self.driver.find_element(by='xpath', value='//*[@id="post-2192"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span/bdi')
                basket=basketValue.text

                self.assertEqual("46,99 zł", basket, "Tekst nie jest zgodny z oczekiwanym")

                self.driver.quit()

if __name__ == "__main__":
    unittest.main()