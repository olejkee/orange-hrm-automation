from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from base.base_class import Base
from metaclasses.meta_locator import MetaLocator

class PimPage(Base, metaclass=MetaLocator):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    pim_page_title = '//h6[text()="PIM"]'
    add_button = '//button[text()=" Add "]'
    input_add_first_name = '//input[@name="firstName"]'
    input_add_last_name = '//input[@name="lastName"]'
    input_add_employee_id = '//div[@class="oxd-grid-2 orangehrm-full-width-grid"]//input[@class="oxd-input oxd-input--active"]'
    save_button = '//button[text()=" Save "]'
    search_input_employee_name = '//input[@placeholder="Type for hints..."]'
    search_button = '//button[text()=" Search "]'
    found_employee_id = '(//div[@class="oxd-table-cell oxd-padding-cell"]//div)[3]'
    found_employee_first_name = '(//div[@class="oxd-table-cell oxd-padding-cell"]//div)[4]'
    found_employee_last_name = '(//div[@class="oxd-table-cell oxd-padding-cell"]//div)[5]'
    
    # URLs
    pim_menu_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'
    pim_add_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'

    # Universal getter
    def get_element(self, locator):
        by, value = getattr(self, locator)
        selenium_by = By.XPATH if by == "xpath" else By.CSS_SELECTOR
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((selenium_by, value))
        )

    # Actions
    def click_pim_menu(self):
        """Navigate to PIM page"""
        self.driver.get(self.pim_menu_url)
        print("Navigating to PIM page")
        time.sleep(2)
        
    def click_add_button(self):
        """Click the Add button to add a new employee"""
        self.get_element("add_button").click()
        print("Clicked Add button")
        time.sleep(2)
        
    def input_first_name(self, first_name):
        """Input first name in the add employee form"""
        self.get_element("input_add_first_name").send_keys(first_name)
        print(f"Input first name: {first_name}")
        
    def input_last_name(self, last_name):
        """Input last name in the add employee form"""
        self.get_element("input_add_last_name").send_keys(last_name)
        print(f"Input last name: {last_name}")
        
    def input_employee_id(self, employee_id):
        """Input employee ID in the add employee form"""
        employee_id_field = self.get_element("input_add_employee_id")
        # Wait for element to be ready
        time.sleep(1)
        # Clear the field first using Ctrl+A and Backspace for more reliable clearing
        employee_id_field.click()
        employee_id_field.send_keys(Keys.COMMAND + "a")
        time.sleep(0.5)
        employee_id_field.send_keys(Keys.DELETE)
        time.sleep(0.5)
        # Alternative clearing method
        employee_id_field.clear()
        # Send the new employee ID
        employee_id_field.send_keys(employee_id)
        print(f"Input employee ID: {employee_id}")
        
    def click_save_button(self):
        """Click the Save button to save employee data"""
        self.get_element("save_button").click()
        print("Clicked Save button")
        time.sleep(3)
        
    def search_employee(self, first_name):
        """Search for an employee by first name"""
        search_field = self.get_element("search_input_employee_name")
        search_field.clear()
        search_field.send_keys(first_name)
        print(f"Searching for employee with first name: {first_name}")
        time.sleep(1)
        self.get_element("search_button").click()
        print("Clicked Search button")
        time.sleep(2)
        
    def get_found_employee_id(self):
        """Get the ID of the found employee"""
        employee_id = self.get_element("found_employee_id").text
        print(f"Found employee ID: {employee_id}")
        return employee_id
        
    def get_found_employee_first_name(self):
        """Get the first name of the found employee"""
        first_name = self.get_element("found_employee_first_name").text
        print(f"Found employee first name: {first_name}")
        return first_name
        
    def get_found_employee_last_name(self):
        """Get the last name of the found employee"""
        last_name = self.get_element("found_employee_last_name").text
        print(f"Found employee last name: {last_name}")
        return last_name

    # Methods
    def verify_pim_page(self):
        """Verify that we are on the PIM page"""
        self.assert_url(self.pim_menu_url)
        page_title = self.get_element("pim_page_title").text
        self.assert_word(page_title, "PIM")
        print("Verified PIM page")
        
    def verify_add_employee_page(self):
        """Verify that we are on the Add Employee page"""
        self.assert_url(self.pim_add_url)
        print("Verified Add Employee page")
        
    def add_employee(self, first_name, last_name, employee_id):
        """Add a new employee with the given details"""
        # Navigate to PIM page
        self.click_pim_menu()
        time.sleep(2)
        self.verify_pim_page()
        
        # Click Add button
        self.click_add_button()
        time.sleep(2)
        self.verify_add_employee_page()
        
        # Fill in employee details
        self.input_first_name(first_name)
        time.sleep(2)
        self.input_last_name(last_name)
        time.sleep(2)
        self.input_employee_id(employee_id)
        time.sleep(2)
        
        # Save employee
        self.click_save_button()
        time.sleep(2) 
        
        # Return to PIM page
        self.click_pim_menu()
        time.sleep(2)  
        self.verify_pim_page()
        
    def verify_employee_in_list(self, first_name, last_name, employee_id):
        """Search for employee and verify details"""
        # Search for employee
        self.search_employee(first_name)
        
        # Get found employee details
        found_id = self.get_found_employee_id()
        found_first_name = self.get_found_employee_first_name()
        found_last_name = self.get_found_employee_last_name()
        
        # Verify details
        assert found_id == employee_id, f"Expected employee ID {employee_id}, but found {found_id}"
        assert found_first_name == first_name, f"Expected first name {first_name}, but found {found_first_name}"
        assert found_last_name == last_name, f"Expected last name {last_name}, but found {found_last_name}"
        
        print(f"Employee verified successfully: {first_name} {last_name} (ID: {employee_id})")