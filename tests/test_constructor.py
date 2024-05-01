from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import URL
from locators import BurgersLocators
from data import get_active_state_button


class TestConstructor():
    def test_active_buns(self, driver):
        driver.get(URL)
        active_button = get_active_state_button()

        driver.find_element(*BurgersLocators.SAUCE).click()
        WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located(BurgersLocators.SAUCE_CONTAINER))

        driver.find_element(*BurgersLocators.BUNS).click()

        assert driver.find_element(*BurgersLocators.BUNS).get_attribute('class') == active_button, "Булки не выбраны"

    def test_active_sauce(self, driver):
        driver.get(URL)
        active_button = get_active_state_button()

        WebDriverWait(driver,15).until(expected_conditions.visibility_of_element_located(BurgersLocators.SAUCE))
        driver.find_element(*BurgersLocators.SAUCE).click()

        assert driver.find_element(*BurgersLocators.SAUCE).get_attribute('class') == active_button, "Соусы не выбраны"

    def test_active_fillings(self, driver):
        driver.get(URL)
        active_button = get_active_state_button()

        #WebDriverWait(driver,15).until(expected_conditions.element_to_be_clickable(BurgersLocators.FILLINGS))
        driver.find_element(*BurgersLocators.FILLINGS).click()

        assert driver.find_element(*BurgersLocators.FILLINGS).get_attribute('class') == BurgersLocators.ACTIVE_STATE_BUTTON, "Начинки не выбраны"

