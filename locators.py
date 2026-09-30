from selenium.webdriver.common.by import By

class Locators:
    #Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    #Ссылка "Зарегистрироваться" ведущая на страницу регистрации
    REGISTER_LINK = (By.CSS_SELECTOR, "a[href='/register']")
    #Заголовок "Регистрация" на странице регистрации
    REGISTRATION_HEADER = (By.XPATH, "//h2[text()='Регистрация']")
    #Поле ввода "Имя" на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    #Поле ввода "Почты" на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    #Поле ввода "Пароль" на странице регистрации
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    #Кнопка "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    #Заголовок страницы "Вход"
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    #Сообщение об ошибке под полем "Пароль"
    PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")
    #Кнопка "Личный кабинет" на главной странице
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный')]")
    #Кнопка "Войти" на странице авторизации
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    #Ссылка "Восстановить пароль" на странице авторизации
    RECOVER_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    #Кнопка "Выйти" в личном кабинете (если вход успешный)
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")
    #Кнопка"Оформить заказ" на главной странице (для проверки входа)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    #Ссылка "Войти" на странице регистрации
    LOGIN_LINK_ON_REGISTER_PAGE = (By.XPATH, "//a[text()='Войти']")
    #Ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK_ON_RECOVER_PAGE = (By.XPATH, "//a[text()='Войти']")
    #Заголовок "Восстановление пароля"
    RECOVER_PASSWORD_HEADER = (By.XPATH, "//h2[text()='Восстановление пароля']")
    #Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    #Кнопка "История заказов" в Личном кабинете
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    #Логотип Stellar Burgers
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")
    #Заголовок "Собери бургер" на главной странице
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    #Булки вкладка
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::*")
    #Заголовок раздела "Булки"
    BUNS_HEADER = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
    #Соусы
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    #Заголовок "Соусы"
    SAUCES_HEADER = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
    #Начинки
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    #Заголовок "Начинки"
    FILLINGS_HEADER = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
    