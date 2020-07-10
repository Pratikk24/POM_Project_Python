from selenium import webdriver
from Libraries.LIB_LoginPage import Loginpage
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
        login = Loginpage(driver)
        login.enter_username(self.qc_username)
        login.enter_password(self.qc_password)
        login.click_login()
        time.sleep(4)

    def test_02_claim_list_page_validation(self):
        self.assertEqual(Locators.title, self.driver.title)

    def test_03_open_case_by_clicking(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.open_case_by_clicking()
        time.sleep(4)

    def test_04_click_on_all_doc_icon(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_all_doc_icon()

    def test_05_click_all_tabs_in_all_doc_section(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_all_doc_tabs()

    def test_06_click_on_back_button(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_back_button()

    def test_07_verify_case(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.verify_case()
        time.sleep(3)

    def test_08_logout(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_three_dot_icon()
        time.sleep(2)
        homepage.click_on_logout()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



