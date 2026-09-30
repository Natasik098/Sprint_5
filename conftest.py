import pytest
from selenium import webdriver
from faker import Faker

fake = Faker()

@pytest.fixture
def generate_email():
    random_digits = fake.random_int(min=1000,max=9999)
    return f"nataliya_kokorina_55{random_digits}@yandex.ru"

@pytest.fixture
def generate_password():
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

@pytest.fixture
def generate_short_password():
    return fake.password(length=5)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
