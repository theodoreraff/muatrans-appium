from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class FormMuatanPage(BasePage):
    """
    Form Muatan page object for Muatrans app
    """
    
    def __init__(self, driver):
        super().__init__(driver)
        # Using a more generic approach to verify page is loaded
        # Wait for the app to be fully loaded by checking for any common UI element
        self.wait_for_page_to_load((AppiumBy.ID, "android:id/content"))
    
    def isi_waktu_muat(self):
        """
        Handle the "Waktu Muat" interaction in the muatrans form
        """
        self.logger.info("Starting Waktu Muat interaction")
        
        try:
            # 1. Tap on the calendar icon
            self.logger.info("Tapping on calendar icon")
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                    "new UiSelector().className(\"android.widget.ImageView\").instance(12)").click()
            
            # 2. Tap on a specific calendar view
            self.logger.info("Tapping on calendar view")
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                    "new UiSelector().className(\"android.view.View\").instance(10)").click()
            
            # 3. Choose delivery type "Instan"
            self.logger.info("Selecting delivery type 'Instan'")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Instan").click()
            
            # 4. Tap "Pilih Tanggal & Waktu Muat"
            self.logger.info("Tapping 'Pilih Tanggal & Waktu Muat'")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Pilih Tanggal & Waktu Muat").click()
            
            # 5. Select date (7 Oktober 2025)
            self.logger.info("Selecting date '7, Selasa, 7 Oktober 2025'")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "7, Selasa, 7 Oktober 2025").click()
            
            # 6. Tap OKE (twice)
            self.logger.info("Tapping OKE button (first time)")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OKE").click()
            
            self.logger.info("Tapping OKE button (second time)")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OKE").click()
            
            # 7. Tap Simpan
            self.logger.info("Tapping Simpan button")
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Simpan").click()
            
            self.logger.info("Completed Waktu Muat interaction successfully")
            
        except Exception as e:
            self.logger.error(f"Error during Waktu Muat interaction: {str(e)}")
            self.take_screenshot("waktu_muat_error")
            raise