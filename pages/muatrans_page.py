from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MuatransPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_muatrans_menu(self):
        print("Navigating to the Muatrans menu...")
        muatrans_button = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Muatrans"))
        )
        muatrans_button.click()
