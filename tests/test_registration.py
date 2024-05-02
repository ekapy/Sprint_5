from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators
from helpers import get_sign_up_data


class TestBurgersRegistration:
    def test_sign_up_success(self, driver):
        driver.get(f'{URL}/register')
        email_data, password_data = get_sign_up_data()

        #Регистрация
        driver.find_element(*BurgersLocators.NAME_FIELD).send_keys("testkatepython")
        driver.find_element(*BurgersLocators.EMAIL_REG_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_REG_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SIGN_UP_BUTTON).click()

        #Ожидание кнопки Войти после регистрации
        WebDriverWait(driver,15).until(expected_conditions.visibility_of_element_located(BurgersLocators.SIGN_IN_BUTTON))

        #Авторизация по ранее зарегистрированным данным
        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()

        #Ожидание кнопки Личный кабинет
        WebDriverWait(driver,15).until(expected_conditions.visibility_of_element_located(BurgersLocators.ACCOUNT_BUTTON))

        #Переход в Профиль
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()

        #Ожидание поля Имя в Профиле
        WebDriverWait(driver,15).until(expected_conditions.visibility_of_element_located(BurgersLocators.PROFILE_NAME))

        #Проверка наличия элемента Имя в Профиле
        assert driver.find_element(*BurgersLocators.PROFILE_NAME).text == "Имя"

    def test_sign_up_empty_name(self, driver):
        driver.get(f'{URL}/register')
        email_data, password_data = get_sign_up_data()

        #Регистрация без заполнения поля Имя
        driver.find_element(*BurgersLocators.EMAIL_REG_FIELD).send_keys(email_data)
        driver.find_element(*BurgersLocators.PASSWORD_REG_FIELD).send_keys(password_data)
        driver.find_element(*BurgersLocators.SIGN_UP_BUTTON).click()

        #Ожидание, что после клика остаемся на Регистрации
        WebDriverWait(driver, 15).until_not(expected_conditions.url_to_be(URL))

        #Проверка, что текущий урл Регистрации
        assert driver.current_url == f'{URL}/register'

    def test_sign_up_invalid_email(self, driver):
        driver.get(f'{URL}/register')

        #Регистрация с невалидным email
        driver.find_element(*BurgersLocators.EMAIL_REG_FIELD).send_keys('testkatepython')
        driver.find_element(*BurgersLocators.PASSWORD_REG_FIELD).send_keys('123456')
        driver.find_element(*BurgersLocators.SIGN_UP_BUTTON).click()

        WebDriverWait(driver, 15).until_not(expected_conditions.url_to_be(URL))

        assert driver.current_url == f'{URL}/register'


    def test_sig_up_password_error(self, driver):
        driver.get(f'{URL}/register')

        #Регистрация с паролем с 5-ю символами
        driver.find_element(*BurgersLocators.EMAIL_REG_FIELD).send_keys('testkatepython@mailinator.com')
        driver.find_element(*BurgersLocators.PASSWORD_REG_FIELD).send_keys('12345')
        driver.find_element(*BurgersLocators.SIGN_UP_BUTTON).click()

        assert driver.find_element(*BurgersLocators.PASSWORD_ERROR).is_displayed()










