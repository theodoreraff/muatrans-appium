import pytest
from pages.form_muatan_page import FormMuatanPage

class TestFormMuatan:
    """
    Test class for Form Muatan functionality
    """
    
    def test_waktu_muat_interaction(self, driver):
        """
        Test the Waktu Muat interaction in the muatrans form
        """
        # Initialize FormMuatanPage
        form_muatan_page = FormMuatanPage(driver)
        
        # Perform the Waktu Muat interaction
        form_muatan_page.isi_waktu_muat()
        
        # Add assertions here to verify the interaction was successful
        # For example, check if a confirmation message is displayed
        # or if the form has been updated with the selected values