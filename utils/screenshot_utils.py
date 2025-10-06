import os
import time
from datetime import datetime

def take_screenshot(driver, test_name):
    """
    Take screenshot and save it to screenshots directory
    
    Args:
        driver: Appium driver instance
        test_name: Name of the test for the screenshot filename
        
    Returns:
        str: Path to the saved screenshot
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    
    # Create screenshots directory if it doesn't exist
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    # Generate filename with test name and timestamp
    filename = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshot_dir, filename)
    
    # Take screenshot
    driver.save_screenshot(screenshot_path)
    
    return screenshot_path