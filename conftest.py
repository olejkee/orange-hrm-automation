# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pages.LoginPage import LoginPage


@pytest.fixture(scope="session")
def chrome_options():
    """Chrome options fixture"""
    options = Options()
    options.add_argument("--guest")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # Remove detach option for automated runs
    # options.add_experimental_option("detach", True)
    return options


@pytest.fixture(scope="function")
def driver(chrome_options):
    """WebDriver fixture"""
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """WebDriver fixture with logged in user"""
    login_page = LoginPage(driver)
    login_page.successful_authorization()
    return driver


@pytest.fixture(scope="function")
def test_data():
    """Test data fixture"""
    return {
        "username": "Admin",
        "password": "admin123",
        "first_name": "John",
        "last_name": "Doe",
        "employee_id": "12345"
    }


@pytest.fixture(scope="function")
def pim_test_data():
    """Specific test data for PIM tests"""
    import random
    return {
        "first_name": "TestUser",
        "last_name": "AutoTest",
        "employee_id": str(random.randint(10000, 99999))
    }