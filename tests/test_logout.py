from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from config import URL
from locators import BurgersLocators
from data import get_sign_in_data


class TestLogout:
    def test_logout_from_profile(self, driver):
        driver.get(f'{URL}/login')
        email, password = get_sign_in_data()

        #Авторизация
        driver.find_element(*BurgersLocators.EMAIL_AUTH_FIELD).send_keys(email)
        driver.find_element(*BurgersLocators.PASSWORD_AUTH_FIELD).send_keys(password)
        driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).click()
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()

        #Переход в Профиль
        driver.find_element(*BurgersLocators.ACCOUNT_BUTTON).click()

        #Логаут
        driver.find_element(*BurgersLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver,15).until(
            expected_conditions.visibility_of_element_located(BurgersLocators.SIGN_IN_BUTTON)
        )
        assert driver.find_element(*BurgersLocators.SIGN_IN_BUTTON).text == "Войти"


