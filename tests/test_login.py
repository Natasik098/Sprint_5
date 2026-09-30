import pytest 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from locators import Locators
from conftest import generate_email, generate_password 

class TestEntrance:
    def test_login_via_main_page_button(self,driver):
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        test_email = "nataliyakokorina55123@yandex.ru"
        test_password = "1q2w3ee3w2q1"

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(test_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(test_password)

        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
        order_button = driver.find_element(*Locators.ORDER_BUTTON)

        assert URLs.BASE_URL in driver.current_url and order_button.text == 'Оформить заказ'

#вход через кнопку «Личный кабинет»
    def test_login_via_personal_account_button(self, driver):
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER)).text == "Вход"

#вход через кнопку в форме регистрации
    def test_login_via_register_page_button(self, driver):
        driver.get(URLs.BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_HEADER))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_LINK_ON_REGISTER_PAGE)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        assert driver.find_element(*Locators.LOGIN_HEADER).text == 'Вход'

#вход через кнопку в форме восстановления пароля
    def test_login_via_recorder_password_page_button(self, driver):
        driver.get(URLs.BASE_URL)        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.RECOVER_PASSWORD_LINK)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.RECOVER_PASSWORD_HEADER))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_LINK_ON_RECOVER_PAGE)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))

        assert driver.find_element(*Locators.LOGIN_HEADER).text =='Вход'
