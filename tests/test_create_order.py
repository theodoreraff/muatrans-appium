from pages.muatrans_page import MuatransPage

def test_create_order(driver):
    muat = MuatransPage(driver)
    # muat.open_muatrans_menu()
    # muat.set_instant_loading_time()
    # muat.input_loading_location()
    # muat.input_unloading_location()
    # muat.input_goods_information()
    # muat._scroll_down_small()
    # muat.select_truck_information()
    muat.complete_order_details()

