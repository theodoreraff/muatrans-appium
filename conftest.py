import pytest
import os
from utils.driver_setup import init_driver, quit_driver

@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture that provides an Appium driver instance
    The fixture is function-scoped, meaning a new driver is created for each test function
    """
    # Initialize driver
    driver_instance = init_driver()
    
    # Yield the driver to the test
    yield driver_instance
    
    # Teardown: quit driver after test completes
    quit_driver(driver_instance)

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    """
    Session-scoped fixture that runs once before all tests
    Can be used for environment setup
    """
    # Create screenshots directory if it doesn't exist
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    
    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # Create reports directory if it doesn't exist
    reports_dir = "reports"
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    
    yield
    
    # Any session teardown can go here