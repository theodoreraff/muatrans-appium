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

    def set_instant_loading_time(self, date_accessibility_id: str = "8, Rabu, 8 Oktober 2025"):
        print("Setting instant loading time...")

        # Tap 'Pilih Tanggal & Waktu Muat'
        try:
            date_button = self.wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").instance(10)')
                )
            )
            date_button.click()
        except:
            print("Fallback: instance(10) not clickable")

        # Klik "Instan"
        instan_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Instan"))
        )
        instan_button.click()

        # Klik ulang "Pilih Tanggal & Waktu Muat" di bottom sheet
        tanggal_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Pilih Tanggal & Waktu Muat"))
        )
        tanggal_button.click()

        # Pilih tanggal dari date picker
        tanggal_tertentu = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, date_accessibility_id))
        )
        tanggal_tertentu.click()

        # Klik OK di date picker
        ok_button_date = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "OKE"))
        )
        ok_button_date.click()

        # Klik OK di time picker
        ok_button_time = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "OKE"))
        )
        ok_button_time.click()

        # Klik "Simpan"
        simpan_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Simpan"))
        )
        simpan_button.click()

    def input_loading_location(self, location="Graha Airi 101", pic_name="QA Tester", pic_phone="089912341234"):
        print("Filling Loading Location (Lokasi Muat)...")

        # Tap input field 'Masukkan Lokasi Muat'
        location_field = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Masukkan Lokasi Muat"))
        )
        location_field.click()

        # Input location keyword
        search_box = self.wait.until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        search_box.send_keys(location)

        # Pilih hasil suggestion
        suggestion = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,
                                            "Graha Airi, Jalan Kedung Doro, RT.001/RW.06, Kedungdoro, Surabaya, Jawa Timur, Indonesia"
                                            ))
        )
        suggestion.click()

        # Input Nama PIC (EditText instance(1))
        pic_name_field = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(1)'
            ))
        )
        pic_name_field.click()
        pic_name_field.send_keys(pic_name)

        # Input No HP PIC (EditText instance(2))
        pic_phone_field = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(2)'
            ))
        )
        pic_phone_field.click()
        pic_phone_field.send_keys(pic_phone)

        # Tap 'Simpan'
        save_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Simpan"))
        )
        save_button.click()
