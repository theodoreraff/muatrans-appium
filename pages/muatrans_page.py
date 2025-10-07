from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

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

    def input_unloading_location(self, location="Atlas Beach", pic_name="QA Tester", pic_phone="089912341234"):
        print("Filling Unloading Location (Lokasi Bongkar)...")

        # Tap input field 'Masukkan Lokasi Bongkar'
        unload_field = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Masukkan Lokasi Bongkar"))
        )
        unload_field.click()

        # Tap search box
        search_box = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        search_box.click()
        search_box.send_keys(location)

        # Select suggestion based on input
        suggestion = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,
                                            "Atlas Beach Club, Jalan Pantai Berawa, Tibubeneng, Kabupaten Badung, Bali, Indonesia"
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

    def input_goods_information(self, weight="25"):
        print("Filling Goods Information...")

        # Pilih Kategori Barang (instance 19)
        category_item = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(19)'
            ))
        )
        category_item.click()

        # Tap "Barang Jadi"
        finished_goods = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Barang Jadi"))
        )
        finished_goods.click()

        # Tap "Padat"
        solid_type = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Padat"))
        )
        solid_type.click()

        # Pilih Subkategori (instance 18)
        subcategory = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(18)'
            ))
        )
        subcategory.click()

        # Tap "Mebel"
        furniture = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Mebel"))
        )
        furniture.click()

        # Tap field berat muatan (instance 17)
        weight_field = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.EditText").instance(0)'
            ))
        )
        weight_field.click()

        # Input berat muatan
        weight_input = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        weight_input.click()
        weight_input.send_keys(weight)

        # Tap 'Simpan'
        save_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Simpan"))
        )
        save_button.click()

    def select_truck_information(self):
        print("Selecting Truck Information...")

        # Scroll down slightly to reveal Armada section
        self._scroll_down_small()

        # Pilih Jenis Armada (instance 18)
        armada_type = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(18)'
            ))
        )
        armada_type.click()

        # Pilih "Bak Terbuka"
        open_truck = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Bak Terbuka"))
        )
        open_truck.click()

        # Pilih Jenis Truk (instance 20)
        truck_type = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.view.View").instance(20)'
            ))
        )
        truck_type.click()

        # Pilih opsi Medium Truk 4 x 2 (Rigid)
        medium_truck = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().description("Medium Truk 4 x 2 (Rigid)\nRp1.426.375\nEstimasi Kapasitas\n12.5 ton\nEstimasi Dimensi (p x l x t)\n5.5 x 2.4 x 2.0 m")'
            ))
        )
        medium_truck.click()

        # Klik tombol "Lanjut"
        lanjut_button = self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Lanjut"))
        )
        lanjut_button.click()

    def _scroll_down_small(self):
        """Scroll sedikit ke bawah untuk memastikan elemen di bawah layar terlihat."""
        self.driver.execute_script("mobile: scrollGesture", {
            'left': 100,
            'top': 500,
            'width': 300,
            'height': 800,
            'direction': 'down',
            'percent': 0.6
        })
