from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators
from data import get_sign_in_data


class TestProfilePage:
    def test_from_profile_page_to_constructor(self, driver):
        driver.get(f'{URL}/login')
        email, password = get_sign_in_data()

        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*BurgersLocators.CONSTRUKTOR_HEADER).click()

        assert driver.find_element(*BurgersLocators.ORDER_BUTTON).text == 'Оформить заказ'

    def test_click_logo_from_profile_page(self, driver):
        driver.get(f'{URL}/login')
        email, password = get_sign_in_data()

        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()

        driver.find_element(*BurgersLocators.LOGO_HEADER).click()

        assert driver.find_element(*BurgersLocators.ORDER_BUTTON).text == 'Оформить заказ'