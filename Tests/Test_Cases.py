from selenium import webdriver
from Libraries.LIB_LoginPage import Loginpage
from Libraries.LIB_HomePage import Homepage
from Locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
import unittest
import HtmlTestRunner


class Bajaj_claims_test(unittest.TestCase):
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

    def test_01_login_valid(self):
        driver = self.driver
        login = Loginpage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(3)

    def test_02_claim_list_page_validation(self):
        self.assertEqual(Locators.title, self.driver.title)

    def test_03_navigate_to_document_page(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_document_list()
        time.sleep(2)

    def test_04_click_on_upload_document(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_upload_document()

    def test_05_case_upload_successfully_validation(self):
        driver = self.driver
        wait = WebDriverWait(driver, 60)
        wait.until(ec.text_to_be_present_in_element((By.XPATH, Locators.upload_successfully_x_path), Locators.upload_successfully_text))

    def test_06_click_on_close_button(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_close_button()
        time.sleep(5)

    def test_07_click_on_refresh_button(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_refresh_button()

    def test_08_case_create_successfully(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        wait.until(ec.text_to_be_present_in_element((By.XPATH, Locators.file_name_x_path), Locators.file_name))
        wait.until(ec.text_to_be_present_in_element((By.XPATH, Locators.case_state_x_path), Locators.state))

    def test_09_go_to_claim_list_page(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_claims_list()
        time.sleep(3)

    def test_10_select_case(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_select_case()
        time.sleep(2)

    def test_11_allocation_arrow(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_allocation_arrow()
        time.sleep(2)

    def test_12_qc_user_selection(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_qc_user_selection()
        time.sleep(2)

    def test_13_qc_user_allocation(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_qc_user_allocation()
        time.sleep(3)

    def test_14_logout(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_three_dot_icon()
        time.sleep(3)
        homepage.click_on_logout()
        time.sleep(5)

    def test_15_qc_user_login_validation(self):
        driver = self.driver
        login = Loginpage(driver)
        login.enter_username(self.qc_username)
        login.enter_password(self.qc_password)
        login.click_login()
        time.sleep(4)

    def test_16_claim_list_page_validation(self):
        self.assertEqual(Locators.title, self.driver.title)

    def test_17_open_case_by_clicking(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.open_case_by_clicking()
        time.sleep(4)

    def test_18_verify_case(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.verify_case()
        time.sleep(3)

    def test_19_logout(self):
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


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(Locators.output))
