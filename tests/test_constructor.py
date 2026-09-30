from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from locators import Locators

class TestConstructor:
    def test_constructor_go_to_buns(self, driver):
        driver.get(URLs.BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.FILLINGS_SECTION)).click()
        wait.until(EC.visibility_of_element_located(Locators.FILLINGS_HEADER))

        wait.until(EC.element_to_be_clickable(Locators.FILLINGS_SECTION)).click
        wait.until(EC.element_to_be_clickable(Locators.BUNS_SECTION)).click()

        buns_header = wait.until(EC.visibility_of_element_located(Locators.BUNS_HEADER))
        assert buns_header.text == "Булки"

    def test_constructor_go_to_sauces(self, driver):
        driver.get(URLs.BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.SAUCES_SECTION)).click()
        sauces_header = wait.until(EC.visibility_of_element_located(Locators.SAUCES_HEADER))
        assert sauces_header.text == "Соусы"

    def test_constructor_go_to_fillings(self, driver):
        driver.get(URLs.BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(Locators.FILLINGS_SECTION)).click()
        fillings_header = wait.until(EC.visibility_of_element_located(Locators.FILLINGS_HEADER))
        assert fillings_header.text == "Начинки"