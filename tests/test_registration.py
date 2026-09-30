from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import URLs, UserData 

#Форма регистрации
def fill_registration_form(driver, email, password):
    driver.find_element(*Locators.NAME_INPUT).send_keys(UserData.NAME)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

def test_registration_success(driver, generate_password, generate_email):
    driver.get(URLs.BASE_URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
    wait.until(EC.element_to_be_clickable(Locators.REGISTER_LINK)).click()
    wait.until(EC.element_to_be_clickable(Locators.REGISTRATION_HEADER))

    fill_registration_form(driver, generate_email, generate_password)
    wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
    wait.until(EC.visibility_of_element_located(Locators.LOGIN_HEADER))
    assert driver.current_url == URLs.LOGIN_URL

    #Ошибка при регистрации с неккоректным паролем(меньше 6 символов)
def test_registration_incorrect_password(driver, generate_email, generate_short_password):

    driver.get(URLs.REGISTER_URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(Locators.REGISTRATION_HEADER))

    fill_registration_form(driver, generate_email, generate_short_password)
    wait.until(EC.element_to_be_clickable(Locators.REGISTER_BUTTON)).click()
    error_message = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR))
    assert error_message.text == "Некорректный пароль"