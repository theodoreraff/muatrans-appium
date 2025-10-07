from pages.muatrans_page import MuatransPage

def test_create_order(driver):
    muat = MuatransPage(driver)
    muat.open_muatrans_menu()
    muat.set_instant_loading_time()
    muat.input_loading_location()
    muat.input_unloading_location()