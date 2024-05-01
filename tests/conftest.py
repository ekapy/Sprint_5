import pytest
from selenium import webdriver
from config import URL
from data import get_sign_in_data
from locators import BurgersLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import get_sign_in_data

@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.get(URL)
    yield chrome
    chrome.quit()



