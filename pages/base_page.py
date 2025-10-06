from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot_utils import take_screenshot
from utils.logger_utils import get_logger

class BasePage:
    """
    Base class for all page objects
    Contains common methods and properties
    """
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        self.logger = get_logger(self.__class__.__name__)
    
    def find_element(self, locator, timeout=10):
        """
        Find element with explicit wait
        
        Args:
            locator: Tuple of (by, value)
            timeout: Maximum time to wait (seconds)
            
        Returns:
            WebElement: Found element
        """
        by, value = locator
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            self.logger.info(f"Element found: {by}={value}")
            return element
        except Exception as e:
            self.logger.error(f"Element not found: {by}={value}, Error: {str(e)}")
            take_screenshot(self.driver, f"element_not_found_{by}_{value}")
            raise
    
    def find_elements(self, locator, timeout=10):
        """
        Find multiple elements with explicit wait
        
        Args:
            locator: Tuple of (by, value)
            timeout: Maximum time to wait (seconds)
            
        Returns:
            List[WebElement]: List of found elements
        """
        by, value = locator
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((by, value))
            )
            self.logger.info(f"Found {len(elements)} elements: {by}={value}")
            return elements
        except Exception as e:
            self.logger.error(f"Elements not found: {by}={value}, Error: {str(e)}")
            take_screenshot(self.driver, f"elements_not_found_{by}_{value}")
            raise
    
    def click(self, locator, timeout=10):
        """
        Click on element
        
        Args:
            locator: Tuple of (by, value)
            timeout: Maximum time to wait (seconds)
        """
        element = self.find_element(locator, timeout)
        try:
            element.click()
            self.logger.info(f"Clicked element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element: {locator}, Error: {str(e)}")
            take_screenshot(self.driver, f"click_failed_{locator}")
            raise
    
    def enter_text(self, locator, text, clear_first=True, timeout=10):
        """
        Enter text into input field
        
        Args:
            locator: Tuple of (by, value)
            text: Text to enter
            clear_first: Whether to clear the field first
            timeout: Maximum time to wait (seconds)
        """
        element = self.find_element(locator, timeout)
        try:
            if clear_first:
                element.clear()
            element.send_keys(text)
            self.logger.info(f"Entered text '{text}' in element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to enter text in element: {locator}, Error: {str(e)}")
            take_screenshot(self.driver, f"enter_text_failed_{locator}")
            raise
    
    def get_text(self, locator, timeout=10):
        """
        Get text from element
        
        Args:
            locator: Tuple of (by, value)
            timeout: Maximum time to wait (seconds)
            
        Returns:
            str: Element text
        """
        element = self.find_element(locator, timeout)
        try:
            text = element.text
            self.logger.info(f"Got text '{text}' from element: {locator}")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text from element: {locator}, Error: {str(e)}")
            take_screenshot(self.driver, f"get_text_failed_{locator}")
            raise
    
    def is_displayed(self, locator, timeout=10):
        """
        Check if element is displayed
        
        Args:
            locator: Tuple of (by, value)
            timeout: Maximum time to wait (seconds)
            
        Returns:
            bool: True if element is displayed, False otherwise
        """
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()
        except Exception:
            return False
    
    def is_enabled(self, locator, timeout=10):
        """
        Check if element is enabled
        
        Args:
            locator: Tuple of (by, value)
            timeout: Maximum time to wait (seconds)
            
        Returns:
            bool: True if element is enabled, False otherwise
        """
        try:
            element = self.find_element(locator, timeout)
            return element.is_enabled()
        except Exception:
            return False
    
    def get_attribute(self, locator, attribute, timeout=10):
        """
        Get attribute value from element
        
        Args:
            locator: Tuple of (by, value)
            attribute: Attribute name
            timeout: Maximum time to wait (seconds)
            
        Returns:
            str: Attribute value
        """
        element = self.find_element(locator, timeout)
        try:
            value = element.get_attribute(attribute)
            self.logger.info(f"Got attribute '{attribute}'='{value}' from element: {locator}")
            return value
        except Exception as e:
            self.logger.error(f"Failed to get attribute from element: {locator}, Error: {str(e)}")
            take_screenshot(self.driver, f"get_attribute_failed_{locator}")
            raise
    
    def scroll_to_element(self, locator, max_swipes=10):
        """
        Scroll to element (for Android)
        
        Args:
            locator: Tuple of (by, value)
            max_swipes: Maximum number of swipe attempts
            
        Returns:
            WebElement: Found element after scrolling
        """
        by, value = locator
        for i in range(max_swipes):
            if self.is_displayed(locator, timeout=2):
                return self.find_element(locator)
            # Scroll down
            self.driver.execute_script("mobile: scroll", {"direction": "down"})
        
        raise Exception(f"Element not found after {max_swipes} swipes: {locator}")
    
    def wait_for_page_to_load(self, locator, timeout=30):
        """
        Wait for page to load by checking for a specific element
        
        Args:
            locator: Tuple of (by, value)
            timeout: Maximum time to wait (seconds)
        """
        self.find_element(locator, timeout)
        self.logger.info(f"Page loaded successfully, found element: {locator}")
    
    def take_screenshot(self, name):
        """
        Take screenshot with custom name
        
        Args:
            name: Screenshot name
            
        Returns:
            str: Screenshot file path
        """
        return take_screenshot(self.driver, name)