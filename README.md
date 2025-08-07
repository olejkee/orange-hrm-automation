# OrangeHRM Test Automation Project

This project contains automated tests for the OrangeHRM demo application using Python, Selenium WebDriver, and pytest. The tests cover various functionalities of the OrangeHRM system including user authentication, navigation, and employee management.

This automation framework is built using the Page Object Model (POM) design pattern to ensure maintainability and scalability. It includes comprehensive test coverage for core OrangeHRM features with advanced reporting capabilities.


## Project Structure
- `pages/` - Page Object Model classes
- `tests/` - Test cases
- `utilities/` - Helper classes and functions
- [conftest.py](file:///Users/olejah/Desktop/AQA/OrangeHRM/conftest.py) - Pytest configuration and fixtures

## Technologies Used
- Python
- Selenium WebDriver
- Pytest
- Page Object Model design pattern

- ## 🧪 Test Coverage

1. **Authorization Tests**
   - Successful login with valid credentials
   - Unsuccessful login with invalid credentials

2. **Navigation Tests**
   - Left menu navigation (Admin, PIM, Recruitment)

3. **Employee Management Tests**
   - Add new employee
   - Verify employee in employee list

## 🚀 Technologies Used

- Python 3.x
- Selenium WebDriver
- Pytest
- ChromeDriver
- Allure Reports
- Page Object Model design pattern
- Custom metaclass for locator management

## How to Run Tests
```bash
pytest tests/ -v
