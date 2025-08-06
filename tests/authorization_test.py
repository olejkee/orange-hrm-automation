# tests/authorization_test.py
import pytest
from pages.LoginPage import LoginPage
from utilities.logger import Logger

@pytest.mark.order(1)
def test_successful_authorization(driver):
    """Test successful authorization"""
    Logger.add_start_step("test_successful_authorization")
    
    print("========== Starting Authorization Test ==========")
    
    login_page = LoginPage(driver)
    login_page.successful_authorization()
    
    # Verify we're on the dashboard
    assert "dashboard" in driver.current_url
    print("========== Test Passed: Successfully logged in ==========")
    
    Logger.add_end_step(driver.current_url, "test_successful_authorization")

@pytest.mark.order(2)
def test_unsuccessful_authorization(driver):
    """Test unsuccessful authorization"""
    Logger.add_start_step("test_unsuccessful_authorization")
    
    print("========== Starting Unsuccessful Authorization Test ==========")
    
    login_page = LoginPage(driver)
    login_page.unsuccessful_authorization()
    
    # Verify we're still on the login page (or got an error message)
    assert "login" in driver.current_url
    print("========== Test Passed: Correctly handled failed login ==========")
    
    Logger.add_end_step(driver.current_url, "test_unsuccessful_authorization")