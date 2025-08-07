from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time

from base.base_class import Base
from metaclasses.meta_locator import MetaLocator   

class MainPage(Base, metaclass=MetaLocator):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators Left Menu

    admin_menu = '//span[text()="Admin"]'
    pim_menu = '//span[text()="PIM"]'
    recruitment_menu = '//span[text()="Recruitment"]'
    admin_menu_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    pim_menu_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
    recruitment_menu_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates'


     # Универсальный геттер
    def get_element(self, locator):
        by, value = getattr(self, locator)
        selenium_by = By.XPATH if by == "xpath" else By.CSS_SELECTOR
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((selenium_by, value))
        )


   # Actions

    def click_admin_menu(self):
        with allure.step("Click Admin menu"):
            self.get_element("admin_menu").click()
            print('click admin menu')
            time.sleep(2)
            if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers":
                print('перешли в admin menu')
            else:
                print('admin menu не открылся')
            time.sleep(2)

    def click_pim_menu(self):
        with allure.step("Click PIM menu"):
            self.get_element("pim_menu").click()
            print('click pim menu')
            if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList":
                print('перешли в pim menu')
            else:
                print('pim menu не открылся')
            time.sleep(2)

    def click_recruitment_menu(self):
        with allure.step("Click Recruitment menu"):
            self.get_element("recruitment_menu").click()
            print('click recruitment menu')
            if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates":
                print('перешли в recruitment menu')
            else:
                print('recruitment menu не открылся')
            time.sleep(2)

    # Methods

    def test_left_menu(self):
        with allure.step("Test left menu"):
            self.click_admin_menu()
            self.assert_url(self.admin_menu_url)
            self.click_pim_menu()
            self.assert_url(self.pim_menu_url)
            self.click_recruitment_menu()
            self.assert_url(self.recruitment_menu_url)