# tests/left_menu_test.py
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.LoginPage import LoginPage
from pages.Main_Page import MainPage
from utilities.logger import Logger

@pytest.mark.order(3)
@allure.title("Test left menu")
def test_left_menu():
    Logger.add_start_step("test_left_menu")
    
    print("Start test")

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    driver = webdriver.Chrome(options=options)

    login = LoginPage(driver)
    login.successful_authorization()
    
    main = MainPage(driver)
    main.test_left_menu()

    print("========== Test Passed: Left menu navigation successful ==========")
    Logger.add_end_step(driver.current_url, "test_left_menu")
    
    driver.close()