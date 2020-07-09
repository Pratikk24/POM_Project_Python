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
import requests
import json
import jsonpath



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

    def test_01_upload_file(self):
        url1 = "http://claim-portal-bajaj-dev.qa.i3systems.in/integrations/case-data/"
        # reading from file
        file = open('C:/Users/Pratik/PycharmProjects/Claims-POM/Tests/payload', 'r')
        payload = file.read()

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token 0cc04b1e050de4a4b559bdc6ce634bbbb0d510d3'
        }

        response = requests.request("POST", url1, headers=headers, data=payload)

        print(response.text.encode('utf8'))

        response_json = json.loads(response.text)

        i3caseid = jsonpath.jsonpath(response_json, 'data.i3_case_id')

        print(i3caseid)

        url2 = "http://claim-portal-bajaj-dev.qa.i3systems.in/integrations/upload-document/" + str(
            i3caseid[0]) + "__3fa1a63ccd64aff1389d9b86a754eff5.zip"

        # reading from file

        # payload = "<file contents here>"
        print(url2)
        fin = open('C:/Users/Pratik/PycharmProjects/Claims-POM/Tests/O210328.zip', 'rb')
        print(fin.name)
        # files = {'file': fin}
        data = fin.read()
        headers = {
            'Content-Type': 'application/binary',
            'Authorization': 'Token 0cc04b1e050de4a4b559bdc6ce634bbbb0d510d3'
        }

        response = requests.request("POST", url2, headers=headers, data=data)

        print(response.text.encode('utf8'))


    def test_02_login_valid(self):
        time.sleep(15)
        driver = self.driver
        login = Loginpage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()
        time.sleep(3)

    def test_03_claim_list_page_validation(self):
        self.assertEqual(Locators.title, self.driver.title)

    def test_04_navigate_to_document_page(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_document_list()
        time.sleep(3)

    def test_05_click_on_refresh_button(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_refresh_button()
        time.sleep(2)

    def test_06_case_create_successfully(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        wait.until(ec.text_to_be_present_in_element((By.XPATH, Locators.case_state_x_path), Locators.state))

    def test_07_go_to_claim_list_page(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_claims_list()
        time.sleep(3)

    def test_08_select_case(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_select_case()
        time.sleep(2)

    def test_09_allocation_arrow(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_allocation_arrow()
        time.sleep(2)

    def test_10_qc_user_selection(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_qc_user_selection()
        time.sleep(2)

    def test_11_qc_user_allocation(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_qc_user_allocation()
        time.sleep(3)

    def test_12_logout(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_three_dot_icon()
        time.sleep(3)
        homepage.click_on_logout()
        time.sleep(5)

    def test_13_qc_user_login_validation(self):
        driver = self.driver
        login = Loginpage(driver)
        login.enter_username(self.qc_username)
        login.enter_password(self.qc_password)
        login.click_login()
        time.sleep(4)

    def test_14_claim_list_page_validation(self):
        self.assertEqual(Locators.title, self.driver.title)

    def test_15_open_case_by_clicking(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.open_case_by_clicking()
        time.sleep(4)

    def test_16_click_on_all_doc_icon(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_on_all_doc_icon()

    def test_17_click_all_tabs_in_all_doc_section(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_all_doc_tabs()

    def test_18_click_on_back_button(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.click_back_button()

    def test_19_verify_case(self):
        driver = self.driver
        homepage = Homepage(driver)
        homepage.verify_case()
        time.sleep(3)

    def test_20_logout(self):
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
