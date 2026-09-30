from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs 
from locators import Locators

class TestNavigation:
    def test_go_to_personal_account(self,driver):
        driver.get(URLs.BASE_URL)
        self._login(driver)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self._wait_for_url(driver, URLs.PROFILE_PATH)

        profile = driver.find_element(*Locators.ORDER_HISTORY)        
        assert profile.text == 'История заказов'

#Переход из личного кабинета в конструктор
    def test_go_to_constructor_by_bytton(self, driver):
        driver.get(URLs.BASE_URL)
        self._login(driver)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self._wait_for_url(driver, URLs.PROFILE_PATH)
        
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        self.assert_constructor(driver)

#Переход в конструктор по логотипу
    def test_go_to_constructor_by_logo(self, driver):
        driver.get(URLs.BASE_URL)
        self._login(driver)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self._wait_for_url(driver, URLs.PROFILE_PATH)
        
        driver.find_element(*Locators.LOGO).click()
        self.assert_constructor(driver)

#Выход из аккаунта
    def test_logout_from_account(self, driver):
        driver.get(URLs.BASE_URL)
        self._login(driver)
        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        self._wait_for_url(driver, URLs.PROFILE_PATH)
        
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        self._wait_for_url(driver, URLs.LOGIN_PATH)

#Авторизация во всех тестах
    def _login(self,driver):
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys("nataliyakokorina55123@yandex.ru")
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("1q2w3ee3w2q1")
        driver.find_element(*Locators.LOGIN_SUBMIT_BUTTON).click()

#Проверка страницы конструктора
    def assert_constructor(self,driver):
        header = WebDriverWait(driver, 10). until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_HEADER))
        assert URLs.BASE_URL in driver.current_url and header.text == 'Соберите бургер'

#Ожидание в  URL указанной части
    def _wait_for_url(self,driver,url_part, timeout=10):
        WebDriverWait(driver, timeout).until(EC.url_contains(url_part))
        assert url_part in driver.current_url



