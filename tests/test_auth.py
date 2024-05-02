from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators
from data import get_sign_in_data


class TestBurgersAuth:
    def test_sign_in_main_page_from_account_button(self, driver):
        driver.get(URL)
        email, password = get_sign_in_data()

        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()

        WebDriverWait(driver,15).until(
            expected_conditions.url_to_be(f'{URL}/login')
        )
        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()

        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))

        assert driver.find_element(*BurgersLocators.ORDER_BUTTON).text == 'Оформить заказ'


    def test_sign_in_main_page_from_auth_button(self, driver):
        driver.get(URL)
        email, password = get_sign_in_data()

        #Ожидание кнопки 'Войти в аккаунт'
        WebDriverWait(driver,15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.AUTH_BUTTON_MAIN_PAGE)
        )
        driver.find_element(*BurgersLocators.AUTH_BUTTON_MAIN_PAGE).click()

        #Ожидание кнопки Войти на странице Авторизации
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.SIGN_IN_BUTTON))

        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()

        #Ожидание кнопки 'Оформить заказ' после авторизации
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))

        assert driver.find_element(*BurgersLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_sign_in_from_sign_up_page(self, driver):
        driver.get(f'{URL}/register')
        email, password = get_sign_in_data()

        driver.find_element(*BurgersLocators.LOGIN_BUTTON_FOOTER).click()

        # Ожидание кнопки Войти на странице Авторизации
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.SIGN_IN_BUTTON))

        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()

        # Ожидание кнопки 'Оформить заказ' после авторизации
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))

        assert driver.find_element(*BurgersLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_sign_in_from_forgot_password_page(self, driver):
        driver.get(f'{URL}/forgot-password')
        email, password = get_sign_in_data()

        driver.find_element(*BurgersLocators.LOGIN_BUTTON_FOOTER).click()
        # Ожидание кнопки Войти на странице Авторизации
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.SIGN_IN_BUTTON))

        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()

        # Ожидание кнопки 'Оформить заказ' после авторизации
        WebDriverWait(driver, 15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.ORDER_BUTTON))

        assert driver.find_element(*BurgersLocators.ORDER_BUTTON).text == 'Оформить заказ'












