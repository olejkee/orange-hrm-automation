# tests/PIM_add_test.py
import pytest
import allure
from pages.PimPage import PimPage
from utilities.logger import Logger

@pytest.mark.order(4)
def test_pim_add_employee(logged_in_driver, pim_test_data):
    """Test to add a new employee and verify it in the employee list"""
    Logger.add_start_step("test_pim_add_employee")
    
    print("========== Starting PIM Add Employee Test ==========")

    try:
        # Initialize PIM page
        pim_page = PimPage(logged_in_driver)
        
        # Get test data
        first_name = pim_test_data["first_name"]
        last_name = pim_test_data["last_name"]
        employee_id = pim_test_data["employee_id"]
        
        print(f"Test data: First Name={first_name}, Last Name={last_name}, Employee ID={employee_id}")

        # Add new employee
        print("Step 2: Adding new employee")
        pim_page.add_employee(first_name, last_name, employee_id)
        
        # Verify employee in list
        print("Step 3: Verifying employee in the list")
        pim_page.verify_employee_in_list(first_name, last_name, employee_id)
        
        print("========== Test Passed: Employee added and verified successfully ==========")
        Logger.add_end_step(logged_in_driver.current_url, "test_pim_add_employee")
        
    except Exception as e:
        print(f"========== Test Failed with error: {str(e)} ==========")
        Logger.write_log_to_file(f"Error in test_pim_add_employee: {str(e)}\n")
        raise e