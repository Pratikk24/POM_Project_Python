from selenium import webdriver
from Libraries.LIB_LoginPage import LoginPage
from Libraries.LIB_HomePage import Homepage
from Locators.locators import Locators
import time
import unittest
import HtmlTestRunner


class QC_user_login(unittest.TestCase):
    url = Locators.url
    username = Locators.Username
    password = Locators.Password
    qc_username = Locators.qc_username
    qc_password = Locators.qc_password

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(Locators.executable_path)
        cls.driver.get(cls.url)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_qc_user_login_validation(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(self.qc_username)
        login.enter_password(self.qc_password)
        login.click_login()
        time.sleep(1)

    def test_02_claim_list_page_validation(self):
        self.assertEqual(Locators.title, self.driver.title)

    def test_03_clear_date_filter(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_clear_date_filter()
        time.sleep(2)

    def test_04_open_case_by_clicking(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.open_case_by_clicking()
        time.sleep(2)

    def test_05_click_on_all_doc_icon(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_all_doc_icon()

    def test_06_click_all_tabs_in_all_doc_section(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_all_doc_tabs()

    def test_07_click_on_back_button(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_back_button()
        time.sleep(2)

    def test_08_non_med_doc_details(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_doc_details()
        time.sleep(1)

    def test_09_nonmed_reports(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_reports()
        time.sleep(1)

    def test_10_medical_details(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_medical_details()
        time.sleep(1)

    def test_11_bills_tab(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_bills_tabs()
        time.sleep(1)

    def test_12_scale(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_scale()
        time.sleep(2)

    def test_13_close_scale(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_close_scale()
        time.sleep(1)

    def test_14_final_bill(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_final_bill()
        time.sleep(1)

    def test_15_close_fulscreen(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_close_fulscreen()
        time.sleep(2)

    def test_16_click_on_npe(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_npe()
        time.sleep(2)

    def test_17_fs(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_fs()
        time.sleep(2)

    def test_18_pharma_details(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_pharma_details()
        time.sleep(2)

    def test_19_patho_details(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_patho_details()
        time.sleep(3)

    def test_20_pharma_amount(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_pharma_amount()
        time.sleep(1)

    def test_21_patho_amount(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.get_patho_amount()
        time.sleep(1)

    def test_22_nonp_amount(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.get_nonp_amount()
        time.sleep(1)

    def test_23_discount_summary(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.get_nonp_amount()
        time.sleep(1)

    def test_24_other_deduction(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.get_nonp_amount()
        time.sleep(1)

    def test_25_backtobills(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_back_to_bills()
        time.sleep(2)

    def test_26_fs_reprocess(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_fs_reprocess()
        time.sleep(2)

    def test_27_backarrow(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_back_arrow()
        time.sleep(1)

    def test_28_verify_case(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.verify_case()
        time.sleep(3)

    def test_29_Logout_from_qc_user(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_three_dot_icon()
        homepage.click_on_logout()

        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

