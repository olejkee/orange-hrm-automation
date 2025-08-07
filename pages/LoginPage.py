# pages/LoginPage.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time

from base.base_class import Base
from metaclasses.meta_locator import MetaLocator

class LoginPage(Base, metaclass=MetaLocator):

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    user_name = '//input[@name="username"]'
    password = '//input[@name="password"]'
    login_button = '//button[@type="submit"]'
    user_menu = '//span[@class="oxd-userdropdown-tab"]'
    logout_button = '//a[text()="Logout"]'
    dashboard_title = '//h6[text()="Dashboard"]'
    unsuccessful_authorization_title = '//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]'

    # Универсальный геттер
    def get_element(self, locator):
        by, value = getattr(self, locator)
        selenium_by = By.XPATH if by == "xpath" else By.CSS_SELECTOR
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((selenium_by, value))
        )

    # Actions
    def input_user_name(self, user_name):
        with allure.step('Input user name'):
            self.get_element("user_name").send_keys(user_name)
            print('Input user name')

    def input_password(self, password):
        with allure.step('Input password'):
            self.get_element("password").send_keys(password)
            print('Input password')

    def click_login_button(self):
        with allure.step('Click login button'):
            self.get_element("login_button").click()
            print('Clicked login button')
            time.sleep(2)
            if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
                print('Authorization was successful')
            else:
                print('Authorization failed')
            time.sleep(2)

    # Methods
    def successful_authorization(self):
        with allure.step("Successful authorization"):
            print('Starting successful authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.input_user_name('Admin')
            self.input_password('admin123')
            self.click_login_button()
            time.sleep(2)
            dashboard_text = self.get_element("dashboard_title").text
            self.assert_word(dashboard_text, 'Dashboard')
            print('Successful authorization completed')

    def unsuccessful_authorization(self):
        with allure.step("Unsuccessful authorization"):
            print('Starting unsuccessful authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.input_user_name('Adminme')
            self.input_password('admin1221')
            self.click_login_button()
            time.sleep(2)
            # Check for error message
            try:
                error_message = self.get_element("unsuccessful_authorization_title").text
                print(f'Error message: {error_message}')
            except:
                print('No error message found')
            print('Unsuccessful authorization completed')