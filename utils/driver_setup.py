from appium import webdriver
from appium.options.android import UiAutomator2Options
import os

def init_driver():
    """
    Initialize an Appium driver using AppiumOptions (W3C compliant)
    for a real Android device using a local Appium server.
    
    Returns:
        webdriver: Appium driver instance
    """
    # Create AppiumOptions instance
    options = UiAutomator2Options()
    
    # Set capabilities
    options.set_capability('platformName', 'Android')
    options.set_capability('appium:deviceName', 'Android Device')
    options.set_capability('appium:automationName', 'UiAutomator2')
    options.set_capability('appium:app', '/home/theodores/muatmuat/mmShipperDEVL_1006202501.apk')
    options.set_capability('appium:autoGrantPermissions', True)
    options.set_capability('appium:appPackage', 'com.azlogistik.muatmuat')
    options.set_capability('appium:appActivity', '.MainActivity')
    options.set_capability('appium:enforceAppInstall', False)
    options.set_capability('appium:ignoreHiddenApiPolicyError', True)
    options.set_capability('appium:noReset', True)
    options.set_capability('appium:fullReset', False)
    options.set_capability('appium:ensureWebviewsHavePages', True)
    options.set_capability('appium:nativeWebScreenshot', True)
    options.set_capability('appium:newCommandTimeout', 3600)
    options.set_capability('appium:connectHardwareKeyboard', True)
    
    # Appium server URL
    appium_server_url = 'http://127.0.0.1:4723'
    
    # Initialize driver
    driver = webdriver.Remote(appium_server_url, options=options)
    
    # Set implicit wait to 10 seconds
    driver.implicitly_wait(10)
    
    return driver

def quit_driver(driver):
    """
    Quit the Appium driver and close the app
    
    Args:
        driver: Appium driver instance
    """
    if driver:
        driver.quit()